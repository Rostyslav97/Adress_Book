from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'home.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'detail.html'

class PersonCreateView(CreateView):
    model=Person
    template_name = 'create.html'
    fields = ['name_surname', 'adress', 'phone']

class PersonUpdateView(UpdateView):
    model=Person
    template_name = 'update.html'
    fields = ['name_surname', 'adress', 'phone']

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home')