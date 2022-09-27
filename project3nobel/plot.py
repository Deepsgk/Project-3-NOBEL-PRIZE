import numpy as py
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
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
from project3nobel.app import app
@app.route("/p_graph.html")
def p_gragh():
  


    df= pd.read_json('/api/v0/nobel1_prize')
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

      return render_template("p_graph.html")
  if __name__ == "__main__":
    app.run()
  