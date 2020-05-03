# Welcome to Django! RecipeBox V1

## Introduction

Django is the most popular Python web framework for making user-facing applications, and it's easy to see why. With the famous tagline of "batteries included" and thousands of plugins on PyPI, it makes sense that you can find it in a lot of platforms.

- The entirety of Instagram is a single monolithic Django app; as of 2016, they leveraged over 50k instances of their software on over 12k machines
- The grand majority of the Washington Post
- Most of USA Today and accompanying sites
- All of Mozilla's support / documentation sites (all that Javascript documentation you were reading a few months ago? That was Django talking!)
- Disqus comments; the plug-and-play comment system is the most popular system of its type, and it's one giant Django app
- Most of Atlassian Bitbucket, a competitor to GitHub and Gitlab
- The entirety of Eventbrite
- The question-and-answer site Quora

Most of these won't advertise that they're looking for "django developers" because they want to make sure that people can work with their stack; instead, they'll focus on finding "python developers". It's up to us to learn how to leverage Django and its vast ecosystem to handle different types of applications.

---

## Instructions


For our introduction, we want to get familiar with creating a new Django application. Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:

- An index page that lists all titles of the loaded recipes (they don't have to be real recipes; just fill them with lorem ipsum and some numbers.)
- Each title is a link that takes you to a single page with the content of that recipe.
- Each detail view for a recipe has the author name.
- Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.
- Make all of the models accessible by the Admin only.

So we have three types of pages: a simple list view, a recipe detail view, and an author detail view. The admin panel will handle the creation views, so we don't need to worry too much about that.

### Important Info:

- Python 3.7, latest version of Django (2.1.2 as of this writing)
- Start a project with `django-admin startproject {project name}` (for example, `django-admin startproject recipebook`)
- Start the server with `python manage.py runserver`
- After you create your models, run `python manage.py makemigrations {foldername}` (where foldername is the top level folder for your project) to create them, then `python manage.py migrate` to push them to the db. If you get stuck, delete the db and run the command again
- If you change your models after running the migrations, run makemigrations and migrate again. If the migrations require the creation of a new table, django will attempt to automatically handle it; if things to weird, `python manage.py migrate --run-syncdb` is your friend
- Create an admin user by running `python manage.py createsuperuser`
- Don't go crazy on the front end. The goal is to just handle the database interactions and basic view path
- Make sure that every detail page (author and recipe) has its own unique URL. If you reload the URL, the same page should appear -- no modals or manipulating the current information on the page. That's too complicated for what we're trying to achieve.
- REITERATING: There are no extra points for pretty HTML! Don't spend time making everything on the front end look gorgeous; we just want to make sure we're serving the right information.

### Author model:

- Name
- User backend (OnetoOne relationship against the Django user)
- Brief Bio section (`TextField`)

### Recipe Model:

- Title
- Author (ForeignKey)
- Description
- Time Required
- Instructions (`TextField`)

If you have any questions or get stuck at any point, don't hesitate to ask. Welcome to a new side of web development! Push up your code to a repo and submit the link to the repo.

---

### Rubric

1. Uses a `models.py` file to contain all database models
2. Uses a `views.py` file to contain all renderable views
3. Does not contain any logic in `models.py`
4. Uses Django template language to create the three primary html files
5. Clicking on a recipe title takes you to the recipe detail page, and clicking on the author name takes you to the author detail page
6. The main page only contains recipe titles
7. The author detail page contains a list of links to all recipes published by that author
8. All models are manipulated from the built-in django admin page
