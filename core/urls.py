from django.urls import path
from .views import HomeView, DetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/categories/<str:categories_id>', HomeView.as_view(), name='categories'),
    path('view/<int:posts_id>', DetailView.as_view(), name='detail'),
]