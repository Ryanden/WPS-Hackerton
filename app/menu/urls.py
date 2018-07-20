from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu-list'),
    path('detail/<int:pk>', views.menu_detail, name='menu-detail')
]
