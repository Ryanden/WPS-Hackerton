from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def menu_list(request):

    return render(request, 'menus/menu_list.html')


def menu_detail(request, pk):

    pass
    # return
