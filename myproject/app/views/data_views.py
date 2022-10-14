from flask import Blueprint, render_template, jsonify, request, redirect, url_for, jsonify, make_response
import sqlite3
import os
import pymysql
import json


bp = Blueprint('data', __name__, url_prefix='/data')


@bp.route('/data', methods=['GET', 'POST'])
def allData():
    if request.method == 'GET':

        con = sqlite3.connect('sensor_data.db')
        cur = con.cursor()
        sql = "SELECT * FROM ID"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        print('==========================')
        data_dict = {}
        
        temp_list = []
        humi_list = []
        illu_list = []

        for row in rows:
            temp_list.append(row[3])
            humi_list.append(row[2])
            illu_list.append(row[1])

        data_dict['temp'] = temp_list
        data_dict['humi'] = humi_list
        data_dict['illu'] = illu_list

        print(data_dict)
        
        data = make_response(json.dumps(data_dict))
        data.content_type = 'application/json'
        
        return data
    








