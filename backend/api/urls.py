from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryViews, name='categories'),
    path('featured/', views.featuredViews, name='featured')
]