import itertools
import os

from flask import Flask, render_template, abort, request
from flask.ext import assets

from whatscooking.database import init_db, db_session
from whatscooking.models.recipes import Recipe
from whatscooking.fixtures import recipe_list, week_list

app = Flask(__name__)
env = assets.Environment(app)

# Tell flask-assets where to look
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'bower_components'),
]

env.register(
    'css_all',
    assets.Bundle(
        'normalize-css/normalize.css',
        'pure/src/base/css/base.css',
        'pure/src/tables/css/tables.css',
        output='all_css.css'
    )
)


@app.route('/')
def home():
    return render_template('home.html.jinja2')


@app.route('/recipes')
def recipes():
    recipe_list = Recipe.query.all()
    return render_template('recipes.html.jinja2', recipes=recipe_list)


@app.route('/recipes/<recipe>')
def get_recipe(recipe):
    s_recipe = filter(lambda x: x['name'] == recipe, recipe_list)

    if not s_recipe:
        abort(404)

    # FIXME: Only checking for first occurrence
    recipe = list(s_recipe)[0]

    return render_template(
        'recipe.html.jinja2',
        name=recipe['name'],
        ingredients=recipe['ingredients'],
        instructions=recipe['steps'])


@app.route('/recipes', methods=['POST'])
def create_recipe():

    # FIXME: Sanitize this
    name = request.form['name']
    r = Recipe(name)

    # FIXME: Names don't have to be unique
    db_session.add(r)
    db_session.commit()

    return r.get_id()


def get_recipe_ingredients(recipe):
    """
    Lookup the ingredients belonging to a recipe
    """

    ingredients = list(itertools.chain.from_iterable([
        i['ingredients']
        for i in recipe_list
        if i['name'] == recipe
    ]))

    return ingredients


@app.route('/thisweek')
def get_week():
    # FIXME: Assummed Sorted
    week = week_list[list(week_list.keys())[-1]]

    week_view = []

    for day, recipes in week.items():
        v_item = {}
        v_item['day'] = day

        # Turn recipes into links?
        v_item['recipes'] = recipes

        # get ingredients from recipe
        v_item['ingredients'] = []
        for r in recipes:
            v_item['ingredients'] = (
                v_item['ingredients'] + get_recipe_ingredients(r))

        week_view.append(v_item)

    days = [day['day'] for day in week_view]
    return render_template('week_view.html.jinja2',
                           week_view=week_view, days=days)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    init_db()

    app.debug = True
    app.run()
