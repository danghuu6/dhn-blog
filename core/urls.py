from django.urls import path
from .views import HomeView, DetailView, CateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('view/<int:posts_id>', DetailView.as_view(), name='detail'),
    path('view-categories/<str:categories_id>', CateView.as_view(), name='cate')
]