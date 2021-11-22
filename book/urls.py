from django.urls import path
from .views import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    path('person/<int:pk>/delete', PersonDeleteView.as_view(), name='delete'),
    path('person/<int:pk>/update',PersonUpdateView.as_view(), name='update'),
    path('person/new/', PersonCreateView.as_view(), name='create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('', PersonListView.as_view(), name='home'),
]