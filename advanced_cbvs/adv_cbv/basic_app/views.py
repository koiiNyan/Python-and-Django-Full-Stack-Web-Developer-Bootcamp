from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView,DetailView
from basic_app import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    # takes the model you called, lowercases everything and then adds _list
    model = models.School
    # returns a list school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    # if no contenxt_obj_name, will return school
    template_name = 'basic_app/school_detail.html'
