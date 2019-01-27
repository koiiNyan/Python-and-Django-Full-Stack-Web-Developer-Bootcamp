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

## STATIC vs MEDIA folders
- Static is stuff that belong to you as a website creator administrator
- Media is stuff that more or less belong to users 
