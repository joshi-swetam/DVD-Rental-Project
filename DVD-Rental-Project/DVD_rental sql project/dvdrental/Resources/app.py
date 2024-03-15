#import dependencies

from pprint import pprint
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect
import psycopg2
import psycopg2.extras
import pandas as pd
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#create connection
conn_string = "host=localhost port=5432 dbname=dvd_rental user=postgres password=PgAdmin123* sslmode=prefer connect_timeout=10"

# use connect function to establish the connection
conn = psycopg2.connect(conn_string)


# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#api route to render api
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the DVD Rental Data Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"===============================================================<br/>"
        f"/api/v1.0/actor_information<br/>"
        f"/api/v1.0/film_information<br/>"
        )
@app.route("/api/v1.0/actor_information")
def get_actor_information():
    #create and empty list
    actor_data = []

 #query to get actor data 
    actor = { 
                "actor_id": "Actor_id"
                , "first_name": "first_name"
                , "last_name": "last_name" 
            } 
    
    actor1 = { 
                "actor_id": "Actor_id1"
                , "first_name": "first_name1"
                , "last_name": "last_name1" 
            } 
                
    actor_data.append(actor)    
    actor_data.append(actor1)

    #return populated list
    return jsonify(actor_data)


if __name__ == '__main__':
    app.run(debug=True)