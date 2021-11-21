import os
import sqlite3
from flask import jsonify
from flask_api import FlaskAPI
from flask_restful import Api
from sqlalchemy import create_engine
from flask import request
import json
app=FlaskAPI(__name__)
api=Api(app)
connection=create_engine('sqlite:///mainballardspahrdb.db')

@app.route('/', methods=['GET'])
def home():
    return json.dumps({'WEBSITE': 'ballardspahr'})

@app.route('/ballardspahrselect', methods=['GET'])
def select():
    connect= connection.connect()
    select= connect.execute("select * from LAWYERTABLE")
    return json.dumps([dict(r) for r in select])

@app.route('/ballardspahrinsert', methods=['GET'])
def insert():
    connect = connection.connect()
    maindata.to_sql('lawyertable',connect,if_exists='replace')
    text = {"Message " : "DATA INSERTED SUCCESSFULLY"}
    return text

@app.route('/ballardspahrcreate', methods=['GET'])
def create():
    try:
        connect = connection.connect()
        trans = connect.begin()
        connect.execute('CREATE TABLE IF NOT EXISTS LAWYERTABLE(SNO INTEGER PRIMARY KEY AUTOINCREMENT,SERVICES TEXT,NAME TEXT,ROLE TEXT,EMAIL TEXT,OFFICES TEXT,TELEPHONE_NUMBER TEXT,FAX_NUMBER TEXT,PAGE_URL TEXT )')
        trans.commit()
        text = {"Message " : "TABLE CREATED SUCCESSFULLY"}
        return text
    except Exception as error:
        text = {"Message " : "TABLE CREATION FAILED"}
        return text
    finally:
        connect.close()
app.run()