from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('main/', views.main_page, name='main_page')
]
