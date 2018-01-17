# menu_app.py
# The application runs here '__main__':
# A menu web application

# IMPORTS #
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# additional set up for Flask and the database
app = Flask(__name__)
engine = create_engine('sqlite:///restaurant_menu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# ROUTING #
# display all restaurants and root
@app.route('/')
@app.route('/restaurants/')
def resaurantDefault():
    output = ""
    output += "Here is the Default Landing Page"
    return output


# App Start
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

