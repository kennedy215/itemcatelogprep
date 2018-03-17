from flask import Flask, render_template, url_for, redirect, request, flash, jsonify, session as login_session
# login_session works like a dictionary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

import random, string

app = Flask(__name__)
app.secret_key = "kennedysecret"

engine = create_engine('sqlite:///restaurantmenu.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def restaurantMenuIndex():
    restaurant = session.query(Restaurant).first()
    item = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    return render_template("index.html", restaurant=restaurant, items=item)


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
# Create a state token to prevent request forgery
# Store it in the session for later validation
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template("login.html", STATE=state)
    #Render the login template


# Export Data and parse into JSON
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems = [i.serialize for i in items])


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
        flash("You've successfully created a new restaurant!!!")
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
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        elif request.form['course']:
            editedItem.course = request.form['course']
        session.commit()
        # return url_for("restaurantMenu", restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)
        flash("Restaurant was edited successfully!")
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id, menu_id=menu_id))
    else:
            # return "page to edit a menu item. Task 2 complete!"
        return render_template("editmenuitem.html", restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem )

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == "POST":
        session.delete(deleteItem)
        session.commit()
        flash("Item was deleted!")
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=deleteItem)




    # return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5556)
