
import numpy as py
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import plotly.express as px
from project3nobel.app import app
from flask import  render_template
@app.route("/p_graph") 
def p_graph():
   
            df= pd.read_json('/nobelprizewinners')
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