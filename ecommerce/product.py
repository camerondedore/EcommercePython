from .static.Product import Product

import json

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('product', __name__)


@bp.route('/')
def index():

    return render_template('product/home.html')


@bp.route('/createproduct', methods=('GET', 'POST'))
def createproduct():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        locations = request.form['locations']

        error = ""

        if not name:
            error = 'Name is required.'
        if not price:
            error += '\nPrice is required.'
        if not quantity:
            error += '\nQuantity is required.'
        if not locations:
            error += '\nLocation is required.'
        if error == "":
            # do something with product later, return to products page

            # create product
            newProduct = Product(name, price, quantity, locations)

            products = []

            # get old list
            with open("test_products.json") as f:
                products = json.load(f)
    
            # add product
            products.append(newProduct)

            fileOutput = open("test_products.json", "w")
            # write to file
            fileOutput.write(json.dumps(products, default=lambda o: o.__dict__))
            # finish file
            fileOutput.close()


            return redirect(url_for('product.products'))

        flash(error)

    return render_template('product/createproduct.html')


@bp.route('/products')
def products():
    return render_template('product/products.html')


@bp.route('/about')
def about():
    return render_template('product/about.html')
