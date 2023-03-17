from django.contrib import admin
from django.urls import path
from myDjangoProjet import views

urlpatterns = [
    path('', views.index)
    , path('index/', views.index)
    , path('checkCourriel/', views.checkCourriel, name='checkCourriel')
    , path('bonjour/', views.bonjour)
    , path('admin/', admin.site.urls)
]
