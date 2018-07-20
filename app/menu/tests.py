from django.test import TestCase, TransactionTestCase

# Create your tests here.
from .models import IceCream


class IceCreamTestCase(TransactionTestCase):

    def create_dummy_data(self):

        icecream = [('바나나맛 아이스크림', '바나나'), ('딸기맛 아이스크림', '딸기')]

        [IceCream.objects.create(name=name, type=type) for name, type in icecream]

    def test_create_ice_cream(self):

        self.create_dummy_data()

        print(IceCream.objects.all())



