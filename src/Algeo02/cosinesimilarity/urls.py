from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='cosinesimilarity-home'),
    path('uploadFile', views.uploadFiles, name='cosinesimilarity-uploadFiles'),
    path('deleteFiles', views.deleteFiles, name='cosinesimilarity-uploadFiles'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('dokumen', views.dokumen, name='file')
]

