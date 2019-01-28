## Class Based Views - "CBV"
- Previously we've created views using functions, however Django provides really powerful tools to use **OOP** and **classes** to define views.
- CBV is used more commonly then functions.
- We will be converting a simple hello function view into a class based view
  * ```from django.views.generic import View```
- Slightly change the way to call a based view in the urls.py
  * **.as_view()** call of the class, which is an inherited method from the View
