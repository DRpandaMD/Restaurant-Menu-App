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
    # returns will now call render_template() to render html files found in /templates/
    return render_template('restaurants.html')


# Create a new restaurant
@app.route('/restaurants/new/')
def restaurant_new():
    return render_template('create_restaurants.html')


# Edit a existing restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/')
def restaurant_edit(restaurant_id):
    return render_template('edit_restaurants.html')


# Delete a specified restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/')
def restaurant_delete(restaurant_id):
    return render_template('delete_restaurants.html')


# show a specific restaurant's menu
@app.route('/restaurants/<int:restaurant_id>/menu/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_show_menu(restaurant_id):
    return render_template('show_menu.html')


# add a new menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def restaurant_new_menu_item(restaurant_id):
    return render_template("create_menu_item.html")


# add a edit menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def restaurant_edit_menu_item(restaurant_id, menu_id):
    return render_template('edit_menu_item.html')


# add a edit menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def restaurant_delete_menu_item(restaurant_id, menu_id):
    return render_template('delete_menu_item.html')


# App Start
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

