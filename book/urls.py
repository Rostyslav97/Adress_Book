from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('post/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('', PersonListView.as_view(), name='home'),
]