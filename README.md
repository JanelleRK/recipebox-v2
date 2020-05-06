# Django Recipebox: Forms!

Welcome to forms in Django!

There's a lot of fun to be had with forms, and thankfully Django takes a lot of the pain and agony away when trying to get data into our application. The video that we took this morning is below, and you can find documentation for what we covered here: [https://docs.djangoproject.com/en/3.0/topics/forms/#building-a-form-in-django] (Links to an external site.)Links to an external site.

Before beginning, make sure you create a new branch off of your local master of recipebox. A good name for your branch may be `dev/forms`.

Now it's time to build some forms the Django way.

Your Task
Make two new html pages for our recipe application: one to add recipes, and one to add authors.
The Django templating language will dynamically render your HTML.
Resource --> [https://docs.djangoproject.com/en/3.0/topics/forms/#the-template] (Links to an external site.)Links to an external site. (note: you will need to make adjustments to the code in the documentation. It will not work without modification).
Make two form classes (contained within forms.py):
These form classes serve as an abstraction of the html form that we will serve to the user in order to receive data from said user.
Your form classes should have the following names:
AddAuthorForm
has appropriate fields as derived from the Author model
AddRecipeForm
has appropriate fields as derived from the Recipe model
Make sure your form classes you are inheriting from django.forms.Form.
After submission, reroute the user to the home page of your application.
Resource --> [https://docs.djangoproject.com/en/3.0/topics/forms/#more-on-fields] (Links to an external site.)Links to an external site.
Make two new views:
add_author 
Uses your AddAuthorForm to create a new author.
add_recipe
Uses your AddRecipeForm to create a new recipe.
Resource --> [https://docs.djangoproject.com/en/3.0/topics/forms/#the-view] (Links to an external site.)Links to an external site.
Make two new endpoints in urls.py:
addauthor/
This will hook up to the view you wrote that uses AddAuthorForm.
addrecipe/
This will hook up to the view you wrote that uses AddRecipeForm.
If you implement all the basic features and have the extra time, feel free to throw in some HTML / CSS and see how that influences your application. If you want to read more about serving static resources, the /static folder may be of some use to you. [https://docs.djangoproject.com/en/3.0/howto/static-files/] (Links to an external site.)Links to an external site.

Demo Video: [https://s3.us-east-2.amazonaws.com/videos.kenzie.academy/Software+Engineering+-+Python/2020-2-3+--+Django+Forms.mp4] (Links to an external site.)Links to an external site.
