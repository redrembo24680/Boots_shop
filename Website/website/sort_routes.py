from Website.website import app
from flask import render_template, url_for, request, redirect
from Website.db import Users, Country, Products
from flask import session as session
from Website.db import session as ses
from datetime import datetime
from sqlalchemy import select
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os


@app.route("/products", methods=['GET'])
def products():
    args = request.args
    name = args.get('name')
    age = args.get('age')
    gender = args.get('gender')

    request_select = None

    request_select = ses.scalars(
        select(Products)
        .where(Products.name.contains(name) if name else Products.name.isnot(None))
        .where(Products.age_category.contains(age) if age else Products.age_category.isnot(None))
        .where(Products.gender.contains(gender) if gender else Products.gender.isnot(None))
    )

    return render_template('adult.html', products=request_select)

