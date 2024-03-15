#import dependencies
import json
from pprint import pprint
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
import pandas as pd
from flask import Flask,render_template


#################################################
# Database Setup
#################################################
#create connection
#conn_string = "host=localhost port=5432 dbname=dvd_rental user=postgres password=PgAdmin123* sslmode=prefer connect_timeout=10"

# use connect function to establish the connection
#conn = psycopg2.connect(conn_string)


# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#api route to render api
def get_db_connection():
    conn_string = "host=localhost port=5432 dbname=dvd_rental user=postgres password=PgAdmin123* sslmode=prefer connect_timeout=10"
    conn = psycopg2.connect(conn_string)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute('SELECT actor_id, first_name, last_name FROM actor')
    res = cur.fetchall()
    return json.dumps(res)


if __name__ == '__main__':
    app.run(debug=True)
