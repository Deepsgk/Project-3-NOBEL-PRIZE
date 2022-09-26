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
def nobel1_prize():
    list= []
    dict ={}
    results = db.session.query(nobel1_prize.awardyear, nobel1_prize.category, nobel1_prize.categoryfullname,
                               nobel1_prize.sortorder, nobel1_prize.prizeamount, nobel1_prize.motivation, 
                               nobel1_prize.award_link, nobel1_prize.id, nobel1_prize.name, nobel1_prize.fullname, nobel1_prize.gender,
                               nobel1_prize.laureate_link, nobel1_prize.birth_date, nobel1_prize.birth_citynow, nobel1_prize.continent,
                               nobel1_prize.countrynow, nobel1_prize.birth_locationstring).all()
                               
   
    for i in range(len(results)):
             
          dict = {
                "awardyear"        : results[i][0],
                "category"         : results[i][1],
                "categoryfullname" : results[i][2],
                "sortorder"        : results[i][3],
                "prizeamount"      : results[i][4],
                "motivation"       : results[i][5],
                "award_link"       : results[i][6],
                "id"               : results[i][7],
                "name"             : results[i][8],
                "fullname"         : results[i][9],
                "gender"           : results[i][10],
                "laureate_link"    : results[i][11],
                "birth_date"       : results[i][12],
                "birth_citynow"    : results[i][13],
                "continent"        : results[i][14],
                "countrynow"       : results[i][15],
                "birth_locationstring" : results[i][16]
            }

    list.append(dict)

    return jsonify(list)  

@app.route("/api/v0/country")
def country():
    results = db.session.query(country.id, country.firstname, country.surname, country.borncountry, country.borncountrycode,
                               country.borncity, country.gender, country.year, country.category, country.motivation,
                               country.organization_name, country.organization_city, country.organization_country,
                               country.latitude, country.longitude).all()
                               
    list= []
    dict ={}
   
    for i in range(len(results)):
             
          dict = {
                "id"              : results[i][0],
                "firstname"       : results[i][1],
                "surname"         : results[i][2],
                "borncountry"     : results[i][3],
                "borncountrycode" : results[i][4],
                "borncity"        : results[i][5],
                "gender"          : results[i][6],
                "year"            : results[i][7],
                "category"        : results[i][8],
                "motivation"      : results[i][9],
                "organization_name" : results[i][10],
                "organization_city" : results[i][11],
                "organization_country": results[i][12],
                "latitude"  : results[i][13],
                "longitude"  : results[i][14]
                
            }

    list.append(dict)

    return jsonify(list)  


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
  


