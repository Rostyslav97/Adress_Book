from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'home.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'

class PersonCreateView(CreateView):
    model=Person
    template_name = 'person_new.html'
    fields = ['name_surname', 'adress', 'phone']