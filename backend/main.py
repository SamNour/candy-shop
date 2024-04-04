from flask import (
    Flask,
    jsonify,
    request,
    make_response,
    render_template,
    redirect,
    url_for,
)
from initDB import (
    init_db_user,
    fetch_user,
    check_db_user,
    check_db_products,
)

from flask_cors import CORS
import sqlite3

app = Flask(__name__)

app.config.from_object(__name__)  # continuly update the app

# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

products_dict = []


@app.route("/products", methods=["GET"])
def get_products():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    products_dict.clear()
    products_dict.extend(
        [
            dict(
                id=row[0],
                name=row[1],
                description=row[2],
                image=row[3],
                price=row[4],
                quantity=row[5],
                user=row[6],
            )
            for row in products
        ]
    )
    for p in products_dict:
        print(p)
    return jsonify(products_dict)


@app.route("/products/<product_id>", methods=["GET"])
def single_game(product_id):
    response_object = {"status": "success", "product": None}
    if request.method == "GET":
        for p in products_dict:
            print(
                f"{p['id']} == {product_id}",
            )
            if p["id"] == int(product_id):  # Conversion to int
                response_object["product"] = p
                return response_object["product"]
    return {"status": "fail", "message": "Product not found"}, 404


@app.route("/update", methods=["PUT"])
def update_product():
    response_object = {"status": "success"}
    put_data = request.get_json()

    user_name, item_id = put_data.get("userName"), put_data.get("itemID")
    # print(put_data)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET user = ?, quantity = quantity + 1 WHERE id = ?",
        (user_name, item_id),
    )
    conn.commit()
    # check_db_products()
    conn.close()
    return jsonify(response_object)


@app.route("/login", methods=["POST"])
def login():
    check_db_user()
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        username = post_data.get("userName")
        password = post_data.get("password")
        print(username, password)
        if username and password:
            user = fetch_user(username, password)
        else:
            response_object["status"] = "fail"
            return jsonify(response_object)
        if user:
            response_object["user"] = user
            response_object["status"] = "success"
        else:
            response_object["status"] = "fail"

    return make_response(jsonify(response_object))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    response_object = {"status": "success", "user": None}
    if request.method == "POST":
        post_data = request.get_json()
        # print(post_data.get("userName") + "  --- " + post_data.get("password"))

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Check if the users table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        )
        if cursor.fetchone() is None:
            # If the users table doesn't exist, initialize the database
            init_db_user(cursor)

        cursor.execute(
            "SELECT * FROM users WHERE username = ?", (post_data.get("userName"),)
        )
        user = cursor.fetchone()

        if user is None:
            # print(type(post_data.get("userName")))
            # print(type(post_data.get("password")))
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (post_data.get("userName"), post_data.get("password")),
            )
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print("[LOG] /signup says := ", row)

        conn.close()
        check_db_user()
        return jsonify(response_object)


@app.route("/search")
def show_search_results():
    query = request.args.get("query")
    return "Search results for: {}".format(query)

        #################################################
        #                                               #
        #       Backend  Server                         # 
        #       Endpoints                               #
        #################################################

"""
document.cookie = 'rolle=whatever';
"""


@app.route("/dev", methods=["GET"])
def show_files_dev():
    cookie_visited_main = request.cookies.get("visited_main")
    cookie_role = request.cookies.get("role")
    if not cookie_visited_main or not cookie_role:
        return redirect("/")
    # if not a wizard redirect to muggles page
    if cookie_role != "admin":
        return render_template("unauthorizedAccess.html")
    return render_template("adminAnalytics.html")


@app.route("/", methods=["GET"])
def show_main_page():
    response = make_response(render_template("main_page.html"))
    response.set_cookie("role", "user")
    response.set_cookie("visited_main", "true")
    return response


@app.route("/docs", methods=["GET"])
def show_API_docs():
    response = make_response(render_template("APIdocs.html"))
    return response


@app.route("/status", methods=["GET"])
def show_status():
    cookie = request.cookies.get("role")
    if cookie != "admin":
        return render_template("unauthorizedAccess.html")
    return render_template("status.html")


if __name__ == "__main__":
    check_db_products()
    app.run(debug=True, port=5000)
