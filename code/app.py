from flask import Flask, jsonify, render_template, redirect
import sqlite3 as sql
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import os

app = Flask(__name__)

# raw_data = Base.classes.raw_data

# Route to render index.html template using data from Mongo
@app.route("/raw_data_list")
def raw_list():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data_list = pd.read_sql("SELECT * FROM raw_data", conn)
    print(raw_data_list)
    return jsonify(raw_data_list.values.tolist())

@app.route("/raw_data")
def raw():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT * FROM raw_data", conn)
    print(raw_data)
    return jsonify(raw_data.to_dict(orient="records"))

@app.route("/unique_countries")
def unique_countries():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT DISTINCT Country FROM raw_data ORDER BY Country ASC", conn)
    print(raw_data)
    return jsonify(raw_data.values.tolist())

@app.route("/top_rated")
def rated():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT * FROM top_rated", conn)
    print(raw_data)
    return jsonify(raw_data.to_dict(orient="records"))

@app.route("/top_votes")
def votes():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT * FROM top_votes", conn)
    print(raw_data)
    return jsonify(raw_data.to_dict(orient="records"))

@app.route("/top_whiskies")
def whiskies():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT * FROM top_whiskies", conn)
    print(raw_data)
    return jsonify(raw_data.to_dict(orient="records"))

@app.route("/raw_data_grouped")
def raw_grouped():
    filepath = os.path.dirname(os.path.abspath(__file__))
    engine = create_engine(f'sqlite:///{filepath}/whisky_dist.db')
    conn = engine.connect()
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # create connection SQLite db
    raw_data = pd.read_sql("SELECT country, count(country) z FROM raw_data where country not in ('Scotland', 'United Kingdom') group by country union select 'United Kingdom', count(country) z from raw_data where country in ('Scotland', 'United Kingdom')", conn)
    print(raw_data)
    return jsonify(raw_data.to_dict(orient="records"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about_us.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True)
