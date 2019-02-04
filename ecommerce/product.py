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

            return redirect(url_for('products.html'))

        flash(error)

    return render_template('product/createproduct.html')
