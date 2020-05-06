from django.shortcuts import render
from recipebox.models import Recipes, Author
from recipebox.forms import AddAuthorForm, AddRecipeForm
from django.shortcuts import redirect

def list_view(request):
    html = "list_view.html"
    items = Recipes.objects.all().order_by("title")
    return render(request, html, {"list": items})


def recipe_detail(request, id):
    html = "recipe_detail.html"
    items = Recipes.objects.all().filter(id=id)
    instructions = items[0].instructions.split("\n")
    return render(request, html,
                  {"recipes": items, "instructions": instructions})


def author_detail(request, id):
    html = "author_detail.html"
    authors = Author.objects.all().filter(id=id)
    items = Recipes.objects.all().filter(author_id=id)
    return render(request, html, {"authors": authors, "recipes": items})


def add_author(request):
    html = "add_author.html"
    form = None
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )
            return redirect('/')
        # return render(request, "author_added.html")
    else:
        form = AddAuthorForm()
    return render(request, html, {"form": form})


def add_recipe(request):
    html = "add_recipe.html"
    form = None
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_req=data["time_req"],
                instructions=data["instructions"],
            )
            return redirect('/')
        # return render(request, "recipe_added.html")
    else:
        form = AddRecipeForm()
    return render(request, html, {"form": form})
