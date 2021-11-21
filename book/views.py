from django.views.generic import ListView, DetailView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'home.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'