## User Authentication
- Built-in tools:
  * Users and the User Model
  * Permissions
  * Groups
  * Passwords and Authentication
  * Logging In and Out

### Passwords
- Setting up the ability to authenticate the User
- Using built-in apps and making sure they're under the **INSTALLED_APPS** list in settings.py
  * django.contrib.auth
  * django.contib.contenttypes
- Remember to migrate if you added them!
- We need to make sure we store our passwords safely
- **NEVER store passwords as plain text!**
- We will begin by using default PBKDF2 algorithm with a SHA256 hash that is built-in to Django
- Installing bcrypt and Argon2 in the virtual environment:
  * pip install bcrypt
  * pip install django[argon2]
- Inside of settings.py pass in the list of PASSWORD_HASHERS to try in the order you want to try them
- Sometimes users will also try to use a very weak password
- We can also add in validator options to prevent a user from doing that

## User Authorization Models
- The User object has a few key features:
  * Username
  * Email
  * Password
  * First Name
  * Surname
- Other User object attributes: is_active, is_staff, is_superuser
- Sometimes you will also want to add more attributes to a user, such as their own links or a profile image
- You can do this in your app's **models.py** by creating another class that has a relationship to the **User** class.
- **Image Field** allows to store images to a model, typically we will keep any user uploaded content like this in the media file.
- In order to work with images with Python we will need to install the Python Image Library:
  * pip install pillow
- After creating the model you need to register it in the admin.py:
  * admin.site.register(UserProfileInfo)
- Next we will want to implement a Django form that the User can use to work with the website

### STATIC vs MEDIA folders
  - Static is stuff that belong to you as a website creator administrator
  - Media is stuff that more or less belong to users
  - Define static and media paths inside settings

## Registration
- A lot of the coding for working with Users and Authorization happens in the **views.py**
- The basic idea is that we check if there is a **POST** request and then perform some sort of action based off that information
- Sometimes we will want to save that information directly to the database
- Other times, we will set *comit=False* so we can manipulate the data before saving it to database
- This helps prevent collision errors of saving the data twice


## LOGIN
- Once the user is registered, we want to make sure that they can log in and out of the site.
- This process involves:
  * Setting up the login views
  * Using built-in decorators for access
  * Adding the LOGIN_URL in settings
  * Creating the login.html
  * Editing the urls.py files
