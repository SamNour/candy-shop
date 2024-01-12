from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)

app.config.from_object(__name__)  # continuly update the app

# allow all domains #TODO: change to only allow localhost http://localhost:8080
CORS(app, resources={r"/*": {"origins": "*"}})


def init_db(cursor):
    cursor.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """
    )

# TODO: create a db table for products, when you know the
# structure of the products table
Products = [
    {
        "id": "1",
        "title": "Smartwatch X1",
        "body": "Advanced fitness tracker with heart rate monitoring and GPS functionality.",
    },
    {
        "id": "2",
        "title": "UltraBook Pro",
        "body": "Lightweight and powerful laptop with a high-resolution display and long battery life.",
    },
    {
        "id": "3",
        "title": "360° Camera Kit",
        "body": "Capture immersive photos and videos with this easy-to-use 360° camera and accessories.",
    },
    {
        "id": "4",
        "title": "Smart Home Hub",
        "body": "Central control unit for smart home devices, enabling seamless automation and remote monitoring.",
    },
    {
        "id": "5",
        "title": "Noise-Canceling Headphones",
        "body": "Immerse yourself in music or work in peace with these high-quality noise-canceling headphones.",
    },
    {
        "id": "6",
        "title": "Professional DSLR Camera",
        "body": "Capture stunning photos and videos with this top-of-the-line digital single-lens reflex camera.",
    },
    {
        "id": "7",
        "title": "Gaming Console X",
        "body": "Experience high-definition gaming with the latest gaming console, featuring cutting-edge graphics and performance.",
    },
    {
        "id": "8",
        "title": "Wireless Charging Pad",
        "body": "Charge your compatible devices wirelessly with this sleek and efficient charging pad.",
    },
    {
        "id": "9",
        "title": "Robotic Vacuum Cleaner",
        "body": "Keep your home clean effortlessly with this smart robotic vacuum cleaner that navigates and cleans on its own.",
    },
    {
        "id": "19",
        "title": "Augmented Reality Glasses",
        "body": "Explore a new dimension with these AR glasses, providing an immersive and interactive experience.",
    },
]


@app.route("/products", methods=["GET"])
def greetings():
    return Products


@app.route("/products/<product_id>", methods=["GET"])
def single_game(product_id):
    response_object = {"status": "success", "product": None}
    if request.method == "GET":
        for p in Products:
            if p["id"] == product_id:  # No conversion to int
                response_object["product"] = p
                return response_object["product"]


@app.route("/login", methods=["POST"])
def login():
    response_object = {"status": "success", "user": None}
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data.get("userName") + "  --- " + post_data.get("password"))

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Check if the users table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        )
        if cursor.fetchone() is None:
            # If the users table doesn't exist, initialize the database
            init_db(cursor)

        cursor.execute(
            "SELECT * FROM users WHERE username = ?", (post_data.get("userName"),)
        )
        user = cursor.fetchone()

        if user is None:
            print(type(post_data.get("userName")))
            print(type(post_data.get("password")))
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (post_data.get("userName"), post_data.get("password")),
            )
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        conn.close()
        check_db()
        return jsonify(response_object)

def check_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Check if the users table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    )
    if cursor.fetchone() is None:
        # If the users table doesn't exist, initialize the database
        init_db(cursor)
    else:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
