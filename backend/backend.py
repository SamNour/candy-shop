from flask import request, make_response, render_template
from backend.main import app

"""
document.cookie = 'rolle=whatever';
"""
@app.route('/dev', methods=['GET'])
def show_files_dev():
    cookie = request.cookies.get('role')
    # if not a wizard redirect to muggles page
    if cookie != 'admin':
        return render_template('unauthorizedAccess.html')
    return render_template('adminAnalytics.html')

@app.route('/', methods=['GET'])
def show_main_page():
    response = make_response(render_template('main_page.html'))
    response.set_cookie('role', 'user')
    return response  

@app.route('/docs', methods=['GET'])
def show_API_docs():
    response = make_response(render_template('APIdocs.html'))
    return response  

@app.route('/status', methods=['GET'])
def show_status():
    cookie = request.cookies.get('role')
    if cookie != 'admin':
        return render_template('unauthorizedAccess.html')
    return render_template('status.html')