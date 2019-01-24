from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Each view is going to have at least one argument.
# Each view must return an HTTP Response Obj.


# Connecting to DB
from first_app.models import Topic, Webpage, AccessRecord
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html',context=date_dict)
