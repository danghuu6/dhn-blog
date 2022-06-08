from django.urls import path
from .views import HomeView, DetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('view/<int:posts_id>', DetailView.as_view(), name='detail'),
]