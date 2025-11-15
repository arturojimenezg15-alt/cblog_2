from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView 
# Create your views here.


class PublicationListView(ListView):
    model = Publication
    template_name = 'home.html'

class PublicationCreteView(CreateView):
    model = Publication
    template_name = 'create.html'
    fields = ['title', 'content', 'author']

class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication_detail.html' 

class PublicationUpdateView(UpdateView):
    model = Publication
    template_name = 'post_update.html'
    fields = ['title', 'content'] 
