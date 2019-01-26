### Django Forms
## Pros:
- Quickly generate HTML form widgets
- Validate data and process it into a Python data structure
- Create form versions of Models, quickly update models from Forms
## Steps to create a form
1. Creating a forms.py inside the application ( proj/ first_app)
2. Call Django's built-in forms Classes (similar to creating Models)
```
from django import forms

class FormName(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  text = forms.CharField(widget=forms.Textarea)
```
3. Show the form by using the views.py ( proj/ first_app)
```
from . import forms
# or
from forms import FormName
```
  * The **.** indicates to import from the same directory as the current .py file

4. Creating a new view for the form
```
def form_name_view(request):
  form = forms.FormName()
  return render(request, 'form_name.html', {'form': form})
```
5. Add the view to the app's urls, either directly or with include()
  * Directly:
  ```
  from basicapp import views
  urlpatterns = [
            url('formpage/'), views.form_name_view, name='form_name'),
  ]
  ```
6. Create the templates folder with the html file that will hold the template tagging
for the form
7. Update settings.py to reflect the **TEMPLATE_DIR** variable
8. Views should reflect subdirectories inside the templates
9. Add the actual template tagging that will create the Django Form  
  * templates/basicapp/form_name.html  
10. There're several ways to "inject" the form using template tagging.
  * pass in the key from the context dictionary:
    * {{ form }}

## HTTP, GET, POST
- **HTTP** - Hypertext Transfer Protocol, designed to enable communication between a
client and a server.
- The client submits a request, the server then responds.
- The most commonly used methods for this request/response protocol are GET and POST
- **GET** - requests data from a resource
- **POST** - submits data to be process to a resource.
## Basic html form
```
<div class="container">
  <form method="POST">
    {{ form.as_p }}
    {% csrf_token %}
    <input type="submit" class="btn btn-primary" value="Submit">
  </form>
</div>
```
- Some added Bootstrap css
- form.as_p uses <p>, returns form within paragraph tags
- You can request a form as a table and work with it that way.
- **CSRF** - Cross-Site Request Forgery token, which secures the HTTP POST action
that is initiated on the subsequent submission of a form.  
It helps protect the user or the website from getting a false data or from a user
accidentally sending the data somewhere else.
  * The Django framework requires the CSRF token to be present
  * If it is not there, your form may not work
  * It works by using a "hidden input" which is a random code and checking that it matches
the user's local site page.
- We need to inform the view that if we get a POST back, we should check if the data is
valid and if so, grab the data (need to edit views)
