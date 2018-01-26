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
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurant=restaurants)


# Create a new restaurant
@app.route('/restaurants/new/', methods=['GET', 'POST'])
def restaurant_new():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('restaurant_default'))
    else:
        return render_template('create_restaurants.html')


# Edit a existing restaurant
@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def restaurant_edit(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        # we want to ensure that the field is filled out
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.update(editedRestaurant)
        session.commit()
        return redirect(url_for('restaurant_default'))
    else:
        return render_template('edit_restaurants.html', restaurant_id=restaurant_id, restaurant=editedRestaurant)


# Delete a specified restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def restaurant_delete(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        return redirect(url_for('restaurant_default'))
    else:
        return render_template('delete_restaurants.html', restaurant_id=restaurant_id, restaurant=restaurantToDelete)


# show a specific restaurant's menu
@app.route('/restaurants/<int:restaurant_id>/menu/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_show_menu(restaurant_id):
    menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    return render_template('show_menu.html', menuItems=menuItems, restaurant_id=restaurant_id, restaurant=restaurant)


# add a new menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def restaurant_new_menu_item(restaurant_id):
    if request.method == 'POST':
        newMenuItem = MenuItem(name=request.form['name'], course=request.form['course'],
                               description=request.form['description'], price=request.form['price'],
                               restaurant_id=restaurant_id)
        session.add(newMenuItem)
        session.commit()
        return redirect(url_for('restaurant_show_menu', restaurant_id=restaurant_id))
    else:
        return render_template("create_menu_item.html", restaurant_id=restaurant_id)


# edit menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def restaurant_edit_menu_item(restaurant_id, menu_id):
    edited_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['course']:
            edited_item.course = request.form['course']
        if request.form['description']:
            edited_item.description = request.form['description']
        if request.form['price']:
            edited_item.price = request.form['price']
        session.add(edited_item)
        session.commit()
        return redirect(url_for('restaurant_show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('edit_menu_item.html', restaurant_id=restaurant_id, menu_id=menu_id, item=edited_item)


# delete a menu item from a restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def restaurant_delete_menu_item(restaurant_id, menu_id):
    item_to_delete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        return redirect(url_for('restaurant_show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item_to_delete)


# App Start
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

