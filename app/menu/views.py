
from django.shortcuts import render
from bs4 import BeautifulSoup


# Create your views here.
from .models import IceCream


def menu_list(request):
    #
    # f = IceCream.objects.all()
    # f.delete()
    # create_db()

    icecream = IceCream.objects.all()

    context = {
        'ice_creams': icecream
    }

    return render(request, 'menus/menu_list.html', context)


def create_db():
    file_path = 'menu/data/ice_cream_list.html'

    html = open(file_path, 'rt').read()

    soup = BeautifulSoup(html, 'lxml')

    ice_cream_list = []

    ul_contents = soup.select("ul.list li")

    img_list = [
        'https://www.baskinrobbins.co.kr/upload/product/1588756610.png',
        'https://www.baskinrobbins.co.kr/upload/product/1591353446.png',
        'https://www.baskinrobbins.co.kr/upload/product/1591353354.png',
        'https://www.baskinrobbins.co.kr/upload/product/1591353167.png',
        'https://www.baskinrobbins.co.kr/upload/product/1541409771.png',
        'https://www.baskinrobbins.co.kr/upload/product/1559783819.png',
        'https://www.baskinrobbins.co.kr/upload/product/1517969437.png',
        'https://www.baskinrobbins.co.kr/upload/product/1554805996.png',
        'https://www.baskinrobbins.co.kr/upload/product/1543739236.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530777439.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530781163.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530777707.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530776851.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530778368.png',
        'https://www.baskinrobbins.co.kr/upload/product/1510020527.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530775359.png',
        'https://www.baskinrobbins.co.kr/upload/product/1530774957.png',
        'https://www.baskinrobbins.co.kr/upload/product/1452062933.png',
    ]
    count = 0

    for li in ul_contents:
        content_name = li.select_one('span')
        content_type = li.select_one('div.hashtag li a')

        if content_name is not None and content_type is not None and count < 17:
            IceCream.objects.create(
                name=content_name.text,
                image=img_list[count],
                type=content_type.text,
            )
            count = count + 1




def menu_detail(request, pk):

    pass
    # return
