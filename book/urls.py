from django.urls import path
from .views import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView

urlpatterns = [
    path('update/<int:pk>/',PersonUpdateView.as_view(), name='update'),
    path('new/', PersonCreateView.as_view(), name='create'),
    path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('', PersonListView.as_view(), name='home'),
]