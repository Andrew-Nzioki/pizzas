#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Pizza,RestaurantPizza,Restaurant




fake = Faker()

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurants = []
    for i in range(20):
        u = Restaurant(name=fake.name(),
                  address=fake.address(),)
        restaurants.append(u)

    db.session.add_all(restaurants)

    pizzas = []
    for i in range(100):
        g =   Pizza(
            name=fake.sentence(),
            ingredients=fake.name(),
           
            price=randint(5, 60),
        )
        pizzas.append(g)

    db.session.add_all(pizzas)

    restaurants_pizzas = []
    for u in restaurants_pizzas:
        for i in range(randint(1, 10)):

            r = RestaurantPizza(
                price=randint(5,60),
                )
            restaurants_pizzas.append(r)

    db.session.add_all(restaurants_pizzas)

    # for g in games:
    #     r = rc(reviews)
    #     g.review = r
    #     reviews.remove(r)

    # db.session.commit()
