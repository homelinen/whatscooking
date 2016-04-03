from flask import Flask, render_template, abort

app = Flask(__name__)


recipe_list = [{
    'name': 'spaghetti bolognese',
    # Can we get the ingredients from the text body?
    'ingredients': [
        'mince',
        'spaghetti',
        'pasata',
        'oregano',
        'garlic',
        'onion'
    ],
    'steps': [
        "Add Oil to a Pan and heat\n",
        "Add mince and onions to the pan and cook until ",
        "browned, stirring occasionally\n",
        "Add pasata, oregano and garlic\n",
        "Boil pasta in a second pot\n"
        "When pasta is cooking mix into the bolognese"
    ]
}]


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


if __name__ == "__main__":
    app.debug = True
    app.run()
