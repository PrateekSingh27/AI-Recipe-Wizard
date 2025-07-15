from django.shortcuts import render
from .forms import IngredientForm
from .ai_model import generate_recipe

def home(request):
    result = ""
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients']
            result = generate_recipe(ingredients)
    else:
        form = IngredientForm()
    return render(request, "home.html", {"form": form, "result": result})
