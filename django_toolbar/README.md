# Django Toolbar
- Panel tools about your project that can help in clarifying why certain behavior is happening
- Can't directly pinpoint the exact source of a bug
- Installing in venv:
  ```
  pip install django-debug-toolbar
  ```
- We need to make changes in `settings.py` to see the toolbar
  * ex: [ProTwo/settings.py](/django_lvl_two/ProTwo)
  * Add to installed apps in settings
    * Note: installed apps are loaded in order that they are listed, so toolbar should be loaded after staticfiles
  * Add toolbar to urls
  * Add to middleware in settings
  * Add internal ip to allow debug tool to know that it should *only* be operating if you're running smth locally.
