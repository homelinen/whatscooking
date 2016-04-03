from flask import Flask, render_template, abort

import itertools

from whatscooking.fixtures import recipe_list, week_list

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html.jinja2')


@app.route('/recipes')
def recipes():
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


if __name__ == "__main__":
    app.debug = True
    app.run()
