import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_db'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories=mongo.db.recipe_categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.recipe_categories.find()
    return render_template("editrecipe.html", recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'description': request.form.get('description'),
        'serves': request.form.get('serves'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'cooking_instructions': request.form.get('cooking_instructions'),
        'prep_time_mins': request.form.get('prep_time_mins'),
        'cook_time_mins': request.form.get('cook_time_mins')
    })
    return redirect(url_for('index'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}),
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/copyrights')
def copyrights():
    return render_template("copyrights.html")





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
