from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")
