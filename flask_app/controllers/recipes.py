from pyexpat import model
from flask import render_template, session, redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models import recipe

bcrypt = Bcrypt(app)

@app.route('/recipe/new')
def recipe_new():
    return render_template("new_recipe.html")

@app.route('/recipe/create', methods=['POST'])
def recipe_create():
    if not recipe.Recipe.validator(request.form):
        return redirect('/recipe/new')
    return redirect('/')