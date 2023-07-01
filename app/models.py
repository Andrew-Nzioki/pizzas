from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules = ('-pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)
#one to many (One restaurant has many Pizzas)
    pizzas=db.relationship('Pizza',backref='restaurant')

# add any models you may need. 
class Pizza(db.Model,SerializerMixin):

    __tablename__='pizzas'
    serialize_rules = ('-restaurants_pizzas.pizza',)

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #pizzas relationship (One to many ,one pizza has many varieties)
    restaurants_pizzas=db.relationship('RestaurantPizza',backref='Pizza')

class RestaurantPizza(db.Model,SerializerMixin):

    __tablename__='restaurant_pizzas'

    serialize_rules = ('-pizza.restaurant_pizzas','-restaurant.restaurant_pizzas')

    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #relationships

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    #extrea step
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', backref='restaurant_pizzas')
