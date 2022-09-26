import pandas as pd
import sqlalchemy
import os
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from flask import Flask, jsonify, render_template, request, url_for, redirect
import sys
import psycopg2
from flask import Response
import json
import plotly.express as px
from flask_sqlalchemy import SQLAlchemy
import os
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite" 

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# flask setup


@app.route("/")
def home():
    return render_template('index.html')  


from .models import ( nobel1_prize,
                     country )

@app.route("/api/v0/nobel1_prize")
def get_nobel1_prize():
    
    results = db.session.query(nobel1_prize.awardyear, nobel1_prize.category, nobel1_prize.categoryfullname,
                               nobel1_prize.sortorder, nobel1_prize.prizeamount, nobel1_prize.motivation, 
                               nobel1_prize.award_link, nobel1_prize.id, nobel1_prize.name, nobel1_prize.fullname, nobel1_prize.gender,
                               nobel1_prize.laureate_link, nobel1_prize.birth_date, nobel1_prize.birth_citynow, nobel1_prize.birth_continent,
                               nobel1_prize.birth_countrynow, nobel1_prize.birth_locationstring).all()
                               
   
             
    nobel1_prize_data = {
                "awardyear"        : [result[0] for result in results],
                "category"         : [result[1] for result in results],
                "categoryfullname" : [result[2] for result in results],
                "sortorder"        :[result[3] for result in results],
                "prizeamount"      :[result[4] for result in results],
                "motivation"       :[result[5] for result in results],
                "award_link"       : [result[6] for result in results],
                "id"               : [result[7] for result in results],
                "name"             : [result[8] for result in results],
                "fullname"         : [result[9] for result in results],
                "gender"           :[result[10] for result in results],
                "laureate_link"    : [result[11] for result in results],
                "birth_date"       : [result[12] for result in results],
                "birth_citynow"    : [result[13] for result in results],
                "birth_continent"        :[result[14] for result in results],
                "birth_countrynow"       : [result[15] for result in results],
                "birth_locationstring" : [result[16] for result in results]
            }


    return Response (nobel1_prize_data.to_json(orient="records"), mimetype='application/json')


@app.route("/api/v0/country")
def get_country_data():
    results = db.session.query(country.id, country.firstname, country.surname, country.borncountry, country.borncountrycode,
                               country.borncity, country.gender, country.year, country.category, country.motivation,
                               country.organization_name, country.organization_city, country.organization_country, country.latitude, country.longitude).all()
                               
    
    country_data = {
                "id"              : [result[0] for result in results],
                "firstname"       : [result[1] for result in results],
                "surname"         : [result[2] for result in results],
                "borncountry"     : [result[3] for result in results],
                "borncountrycode" : [result[4] for result in results],
                "borncity"        : [result[5] for result in results],
                "gender"          :[result[6] for result in results],
                "year"            : [result[7] for result in results],
                "category"        : [result[8] for result in results],
                "motivation"      : [result[9] for result in results],
                "organization_name" : [result[10] for result in results],
                "organization_city" : [result[11] for result in results],
                "organization_country": [result[12] for result in results],
                "latitude"  :[result[13] for result in results],
                "longitude"  :[result[14] for result in results]
                
            }

    return Response(country_data.to_json(orient="records"), mimetype='application/json')

    


# Route for map
@app.route("/map")
def map():
   return render_template("map.html")

@app.route("/d3")
def d3():
   return render_template("d3.html")

@app.route("/app1")
def app1():
   return render_template("app.html")



if __name__ == "__main__":
    app.run()
  


