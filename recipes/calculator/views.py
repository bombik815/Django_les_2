from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def recipes(request):
    context={}
    recipe =request.path
    recipe = recipe.strip('/')
    context['recipe'] = DATA.get(recipe)
    servings = int(request.GET.get('servings', 1))
    for  recipe_, ingredient  in context.items():
        for keys, values in ingredient.items():
            context[recipe_][keys] = values*servings

    return render (request, 'calculator/index.html', context=context)

