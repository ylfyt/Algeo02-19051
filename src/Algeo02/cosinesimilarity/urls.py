from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cosinesimilarity-home'),
    path('search', views.searchResult, name='cosinesimilarity-search'),
    path('about', views.about, name='about'),
]