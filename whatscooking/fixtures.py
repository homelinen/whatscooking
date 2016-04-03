# Data Fixtures for Prototyping

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

week_list = {
    "2016wk3": {
        'Mon': [
            "burgers"
        ],
        'Tue': [
            "spaghetti bolognese"
        ],
        'Wed': [],
        'Thu': [],
        'Fri': [],
        'Sat': [],
        },
    "2016wk4": {
        'Wed': [],
        'Thu': [
            "spaghetti bolognese"
        ],
        'Fri': [],
        'Sat': [
            "pizza"
        ],
        'Sun': [],
        'Mon': [],
    }
}
