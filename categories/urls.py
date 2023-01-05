from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view()),
    path("categories/", views.CategoryCreateView.as_view()),
]
