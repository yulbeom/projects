from flask import Blueprint, render_template, jsonify, request, redirect, url_for, jsonify, make_response
import sqlite3
import json
# from models.graph_model import Database

bp = Blueprint('graph', __name__, url_prefix='/graph')


# 온도
@bp.route('/temp', methods=['POST', 'GET']) 
def tempData():
    if request.method == 'GET':

        con = sqlite3.connect("sensor_data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM ID")
        rows = cur.fetchmany(6)

        print(rows)
        print('==============')
        temp_dict = {} # 온도
        
        temp_list = []
        
        for row in rows:
            print(row)

            temp_list.append(row[3])
            
        temp_dict["temp"] = temp_list

        temp = make_response(json.dumps(temp_dict))
        temp.content_type = 'application/json'    

        print(temp_dict)
        
        return temp
        
        


# 습도
@bp.route('/humi', methods=['POST', 'GET']) 
def humiData():
    if request.method == 'GET':

        con = sqlite3.connect("sensor_data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM ID ")
        rows = cur.fetchmany(6)
        print(rows)
        print('==============')
        
        humi_dict = {} # 습도
        humi_list = []
        
        for row in rows:
            print(row)
            humi_list.append(row[2])
        
        humi_dict["humi"] = humi_list
        
        humi = make_response(json.dumps(humi_dict))
        humi.content_type = 'application/json'
        
        print(humi_dict)
        
        return humi


# 조도
@bp.route('/illu', methods=['POST', 'GET']) 
def illuData():
    if request.method == 'GET':

        con = sqlite3.connect("sensor_data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM ID")
        rows = cur.fetchmany(6)
        
        print(rows)
        print('==============')
        
        illu_dict = {} # 조도
        illu_list = []

        for row in rows:
            print(row)
            illu_list.append(row[1])
            
        illu_dict["illu"] = illu_list

        illu = make_response(json.dumps(illu_dict))
        illu.content_type = 'application/json'

        print(illu_dict)
        
        return illu