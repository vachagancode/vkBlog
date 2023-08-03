from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('only_admin', views.only_admin, name='only_admin'),
    path('about/', views.about_me, name='about')
]