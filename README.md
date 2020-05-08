# Django Recipebox: Authentication!

Django helps us out with a ton of stuff when it comes to starting a website, and authentication is no exception. By hooking into the backend for the admin panel and the helper functions that it gives us, we can roll our own authentication system fairly easily with only a few changes.

Your Task
Note: Make sure you create a new branch off of the `dev/forms` branch we created in the last assessment. Perhaps name it `dev/auth`.

The goal of this assignment is to modify your recipe application to be able to protect those forms; we don't want just anyone adding recipes!

Update the Author model to have a 1-to-1 relationship with the built-in Django User model.
Resources
[https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model] (Links to an external site.)Links to an external site.
[https://docs.djangoproject.com/en/3.0/topics/db/examples/one_to_one/] (Links to an external site.)Links to an external site.
Extend the AddAuthorForm so that we pass usernames and passwords in for user and author accounts to be created.
Add a login page so that people can sign in.
use the @login_required() decorator to lock your form views so that only logged in users can access them... but set them so that they require different permissions to access.
The AddRecipeForm can be accessed by any logged in user.
The AddAuthorForm can only be accessed by admins.
(Hint: check the flag at `request.user.is_staff`)
On your homepage, add a logout button that completes the logout process and dumps the user back on the homepage.
Extra credit, 5 points:

Make the recipe creation page change the Author attribute depending on whether or not the logged-in user is staff or not. If they are staff, list all available Authors as options. If they are not staff, make it so that they can only submit recipes as themselves. 
Demo Video: [https://s3.us-east-2.amazonaws.com/videos.kenzie.academy/Software+Engineering+-+Python/2020-02-05+--+Django+Auth.mp4] (Links to an external site.)Links to an external site.
