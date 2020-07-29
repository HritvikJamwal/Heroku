# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:21:27 2020

@author: hritvik
"""


from flask import Flask,render_template, url_for ,flash , redirect


app=Flask(__name__,template_folder='template', static_folder="static")





@app.route("/")
def home():
    return render_template("index.html")









if __name__ == "__main__":
    app.run()