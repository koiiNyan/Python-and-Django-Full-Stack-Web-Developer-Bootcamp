from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from basic_app import models
from django.urls import reverse_lazy

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

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    # After success deleting
    success_url = reverse_lazy("basic_app:list")
