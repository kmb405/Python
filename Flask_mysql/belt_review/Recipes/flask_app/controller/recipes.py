from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recipes/<int:user_id>')
def recipes(user_id):
    if session['id'] and session['logged_in'] == True:
        recipes = Recipe.get_all_recipes()
        return render_template('recipes.html', recipes=recipes, user_id=user_id)
    else:
        return redirect('/')

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if session['id'] and session['logged_in'] == True:
        recipe = Recipe.get_one_recipe(recipe_id=recipe_id)
        return render_template('recipes_view.html', recipe=recipe)
    else:
        return redirect('/')

@app.route('/recipe/edit/<int:recipe_id>/<int:user_id>')
def recipe(recipe_id, user_id):
    if session['id'] and session['logged_in'] == True:
        return render_template('recipes_edit.html', recipe_id=recipe_id, user_id=user_id)
    else:
        return redirect('/')
    
@app.route('/recipes/new/<int:user_id>')
def create_recipe(user_id):
    if session['id'] and session['logged_in'] == True:
        return render_template('recipes_new.html', user_id=user_id)
    else:
        return redirect('/')

@app.route('/new_recipe', methods=['POST'])
def new_recipe():
    id = request.form['user_id']
    Recipe.create_recipe(request.form)
    return redirect(f'recipes/{id}')

@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    id = request.form['user_id']
    print(request.form)
    recipe_id = Recipe.update_recipe(request.form)
    return redirect(f'recipes/{id}')