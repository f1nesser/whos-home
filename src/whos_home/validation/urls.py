from django.urls import path

from . import views

app_name = 'validation'
urlpatterns = [
    path('', views.index, name='index'),
    path('validate', views.validate, name='validate'),
    path('new_user', views.new_user, name='new_user')
]
