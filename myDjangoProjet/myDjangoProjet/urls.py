from django.contrib import admin
from django.urls import path
from myDjangoProjet import views

urlpatterns = [
    path('', views.index)
    , path('index/', views.index)
    , path('check_courriel/', views.check_courriel, name='check_courriel')
    , path('data_access_sqlite/', views.data_access_sqlite, name='data_access_sqlite')
    , path('data_access_postgresql/', views.data_access_postgresql, name='data_access_postgresql')
    , path('bonjour/', views.bonjour)
    , path('admin/', admin.site.urls)
]
