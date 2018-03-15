from flask import Flask, render_template, url_for, redirect, request, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)
# app.secret_key = "kennedysecret"
engine = create_engine('sqlite:///restaurantmenu.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).first()
    item = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    # output = ''
    # for i in items:
    #     output += i.name
    #     output += '</br>'
    #     output += i.description
    #     output += '</br>'
    #     output += i.price
    #     output += '</br>'
    #     output += '</br>'
    # return render_template("index.html", restaurant=restaurant, items=items)
    return render_template("index.html", restaurant=restaurant, items=item)


# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new', methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
        description=request.form['description'],
        price=request.form['price'],
        course=request.form['course'],
        restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return  redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        # flash("Please type your name!")
        return render_template("newmenuitem.html", restaurant_id=restaurant_id)


# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods = ['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        elif request.form['description']:
            editedItem.description = request.form['description']
        elif request.form['price']:
            editedItem.price = request.form['price']
        elif request.form['course']:
            editedItem.course = request.form['course']
        return url_for("restaurantMenu", restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)
    else:
            # return "page to edit a menu item. Task 2 complete!"
        return render_template("editmenuitem.html", restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem )

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"



    # return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5555)
