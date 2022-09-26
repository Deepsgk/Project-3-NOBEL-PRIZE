import pandas as pd
from flask import Flask, jsonify, render_template, request, url_for, redirect
from requests import session
import psycopg2
import sys
from sqlalchemy import create_engine,SQLAlchemy

import psycopg2
from flask_cors import CORS, cross_origin
from flask import Response
import json
import plotly.express as px
import plotly
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
    return render_template("index.html")  

from .models import ( nobel1_prize,
                     country )

@app.route("/api/v0/nobelprizewinners")
def Nobelprize():
    results = db.session.query(nobel1_prize.awardyear, nobel1_prize.category, nobel1_prize.categortfullname,
                               nobel1_prize.sortorder, nobel1_prize.prizeamount, nobel1_prize.motivation, 
                               nobel1_prize.award_link, nobel1_prize.id, nobel1_prize.name, nobel1_prize.fullname, nobel1_prize.gender,
                               nobel1_prize.laureate_link, nobel1_prize.birth_date, nobel1_prize.birth_citynow, nobel1_prize.continent,
                               nobel1_prize.countrynow, nobel1_prize.birth_locationstring).all()
                               
    list= []
    dict ={}
   
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
def Country():
    results = db.session.query(country.id, country.firstname, country.surname, country.borncountry, country.borncountrycode,
                               country.borncity, country.gender, country.year, country.category, country.motivation,
                               country.organization_name, country.organization_city, country.organization_country, country.lattitude, country.longitude).all()
                               
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
                "longitude"  : results[i][14],
                
            }

        list.append(dict)

    return jsonify(list)  



if __name__ == "__main__":
    app.run()



import numpy as py
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df= pd.read_json('/api/v0/nobelprizewinners')
yearly_prize = df.groupby("awardyear")['awardyear'].count().reset_index(name = 'Count')
fig = px.bar(yearly_prize, x = 'awardyear', y = 'Count')

 

category = df.groupby('category')['category'].count().reset_index(name='Count')
fig2 = px.bar(category, x ='category', y ='Count', color='category')


fig3 = px.histogram(df, x='prizeamount')


fig4 = px.scatter(df, x="prizeamount", y="awardyear", color="category",
           marginal_x="box", template="simple_white")


fig5= px.violin(df,y= "awardyear", x="gender",color="category", box=True)

with open('p_graph.html', 'a') as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))

