from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from recipebox.models import Recipes, Author
from recipebox.forms import AddAuthorForm, AddRecipeForm, LoginForm
from django.shortcuts import redirect
from django.db import IntegrityError

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


@staff_member_required(login_url="/login/")
def add_author(request):
    html = "add_author.html"
    form = None
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # user = User.objects.create_user(
            #     username=data["name"], password='asdfasdf2')
            # Author.objects.create(
            #     name=data["name"],
            #     bio=data["bio"],
            #     user=user
            # )
            try:
                Author.objects.create(
                    name=data["name"],
                    bio=data["bio"],
                    user=data["user"])
                return HttpResponseRedirect(reverse('homepage'))
            except IntegrityError as e:
                if 'unique constraint' in e.args[0]:
                    return render(request, html, {"form": form})
    else:
        form = AddAuthorForm()
    return render(request, html, {"form": form})


@login_required
def add_recipe(request):
    html = "add_recipe.html"
    form = None
    if request.method == "POST":
        form = AddRecipeForm(request.POST, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_req=data["time_req"],
                instructions=data["instructions"],
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = AddRecipeForm(user=request.user)
    return render(request, html, {"form": form})


def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", "/"))
