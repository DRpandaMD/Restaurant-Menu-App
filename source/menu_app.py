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
def restaurant_default():
    output = ""
    output += "Here is the Default Landing Page"
    return output


# Create a new restaurant
@app.route('/restaurants/new/')
def restaurant_new():
    output = ""
    output += "Here is the New Restaurant Page"
    return output


# Edit a existing restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/')
def restaurant_edit(restaurant_id):
    output = ""
    output += "Here is the Edit Restaurant Page"
    return output


# Delete a specified restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/')
def restaurant_delete(restaurant_id):
    output = ""
    output += "Here is the Delete Restaurant Page"
    return output


# show a specific restaurant's menu
@app.route('/restaurants/<int:restaurant_id>/menu/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_show_menu(restaurant_id):
    output = ""
    output += "Here is the Menu for 'x' Restaurant Page"
    return output


# add a new menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def restaurant_new_menu_item(restaurant_id):
    output = ""
    output += "Here is the new menu item for 'x' Restaurant Page"
    return output


# add a edit menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def restaurant_edit_menu_item(restaurant_id, menu_id):
    output = ""
    output += "Here is the edit menu item for 'x' Restaurant Page"
    return output


# add a edit menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def restaurant_delete_menu_item(restaurant_id, menu_id):
    output = ""
    output += "Here is the delete menu item for 'x' Restaurant Page"
    return output


# App Start
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

