from flask import Blueprint, render_template, jsonify, request, redirect, url_for, jsonify
import pymysql


bp = Blueprint('home', __name__, url_prefix='/home')


# ----------------------------------------------- coffee ------------------------------------------------

# navigation bar: home
@bp.route('/homepage')
def navi_home():
    return render_template('homepage.html')

# navigation bar: getstarted
@bp.route('/getstarted')
def navi_getstarted():
    return render_template('getstarted.html')

# navigation bar: guides
@bp.route('/guides')
def navi_guides():
    return render_template('guides.html')

# navigation bar: roasters
@bp.route('/roasters')
def navi_roasters():
    return render_template('roasters.html')

# navigation bar: shop
@bp.route('/shop')
def navi_shop():
    return render_template('shop.html')

# navigation bar: E-agriculture
@bp.route('/E-agriculture')
def navi_agriculture():
    return render_template('E-agriculture.html')

# ------------------------------------ E-agriculture -----------------------------------   

# navigation bar: data
@bp.route('/dashboard')
def navi_dashboard():
    return render_template('dashboard.html')

# navigation bar: data_table (management)
@bp.route('/data')
def navi_data():
    return render_template('data.html')

# navigation bar: data_table (management)
@bp.route('/table')
def navi_table():
    return render_template('table.html')

# navigation bar: data_table (management)
@bp.route('/management')
def navi_management():
    return render_template('management.html')

# navigation bar: A.I
@bp.route('/AI')
def navi_AI():
    return render_template('AI.html')

# navigation bar: graph
@bp.route('/statistics')
def navi_statistics():
    return render_template('statistics.html')

# navigation bar: graph
@bp.route('/controller')
def navi_controller():
    return render_template('controller.html')

# -------------------------------------- options ----------------------------------------

