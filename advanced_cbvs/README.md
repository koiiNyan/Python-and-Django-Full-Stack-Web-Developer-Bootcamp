## Class Based Views - "CBV"
- Previously we've created views using functions, however Django provides really powerful tools to use **OOP** and **classes** to define views.
- CBV is used more commonly then functions.
- We will be converting a simple hello function view into a class based view
  * ```from django.views.generic import View```
- Slightly change the way to call a based view in the urls.py
  * **.as_view()** call of the class, which is an inherited method from the View

## Template Views with CBV
- Templates VS Template View
- Function Based View:  
  ```
  def index(request):
    return render(request, 'index.html')
  ```
- Class Based Template View:  
  ```
  class IndexView(TemplateView):
    template_name = 'index.html'
  ```

- **NOTE!!**
  *  * args - arguments  
  * gives all function parameters as a tuple
  * basically it's a way that you can prepare the function to accept more than one argument:  
  ```
  def foo(*args):
    for a in args:
        print(a)

  foo(1)
  # Prints 1
  foo(1,2,3)
  # Prints:
  # 1
  # 2
  # 3
  ```
  * ** kwargs - key word arguments
  * gives all keyword arguments as a dictionary  
  ```
  def bar(**kwargs):
    for a in kwargs:
      print (a, kwargs[a])

  bar(name='one',age=27)
  # Prints:
  # name one
  # age 27
  ```

## Detail View and List View
- Often when we have models, we want to either list the records from the model, or show details of a single record.
- Django has some generic view classes you can inherit from your model
- It is common practice to have a **template** folder inside the app's folder

## CRUD
- **C** reate **R** etrieve **U** pdate **D** elete
- CRUD is inherit to almost every website
- Whenever you work with models and databases you'll need to perform those four basic actions
- For CreateView we need to specify fields allowed for users to create
