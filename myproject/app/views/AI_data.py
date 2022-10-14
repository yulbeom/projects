from flask import Blueprint, render_template, jsonify, request, redirect, url_for, jsonify, make_response
import sqlite3
import os
import pymysql
import json


bp = Blueprint('A.I', __name__, url_prefix='/A.I')


@bp.route('/output', method=['GET', 'POST'])
def output():
    if request.method == 'GET':

        con = sqlite3.connect('sensor_data.db')
        cur = con.cursor()
        sql = "SELECT * FROM ID"
        cur.execute(sql)
        rows = cur.fetchmany(6)
        print(rows)
        print('==========================')
        data_dict = {}
        
        output_list = []
        
        for row in rows:
            output_list.append(row[0])
            
        data_dict['output'] = output_list
        
        print(data_dict)
        
        data = make_response(json.dumps(data_dict))
        data.content_type = 'application/json'
        
        return data



    
