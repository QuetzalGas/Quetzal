from unittest import TestCase
from .stock import Stock
from .product import *


def giveListofstock(listy, type):
    myList = list()
    if type == 'cll':
        if not listy.isEmpty():
            cur = listy.head
            while cur.next is not listy.dummyhead:
                cur = cur.next
                myList.append(cur.item.get_expiration_date())
    else:
        if not listy.isEmpty():
            cur = listy.head
            for i in range(0, listy.getLength()):
                myList.append(cur.item.get_expiration_date())
                cur = cur.next
    return myList


class testStock(TestCase):
    def testEmptyBeforeAdding(self, type='cll'):
        stock = Stock(type)
        self.assertTrue(stock.is_empty("chilipeper"))
        self.assertTrue(stock.is_empty("honing"))
        self.assertTrue(stock.is_empty("wit"))
        self.assertTrue(stock.is_empty("melk"))
        self.assertTrue(stock.is_empty("bruin"))
        self.assertTrue(stock.is_empty("marshmallow"))

    def testEmptyAfterAdding(self, type='cll'):
        stock = Stock(type)
        stock.add_item(Chocolateshot(2, "wit"))
        stock.add_item(Marshmallow(3))
        stock.add_item(Honey(2))
        stock.add_item(Chilipepper(12))
        stock.add_item(Chocolateshot(52, "bruin"))
        stock.add_item(Chocolateshot(753, "melk"))

        self.assertFalse(stock.is_empty("chilipeper"))
        self.assertFalse(stock.is_empty("honing"))
        self.assertFalse(stock.is_empty("wit"))
        self.assertFalse(stock.is_empty("melk"))
        self.assertFalse(stock.is_empty("bruin"))
        self.assertFalse(stock.is_empty("marshmallow"))

    def testAddAndPop(self, type='cll'):
        stock = Stock(type)
        stock.add_item(Honey(2))
        stock.add_item(Honey(4))
        stock.add_item(Honey(10))
        stock.add_item(Honey(3))
        self.assertEqual([3, 10, 4, 2], giveListofstock(stock.honeyList, type))

        stock.add_item(Chilipepper(3))
        stock.add_item(Chilipepper(4))
        stock.add_item(Chilipepper(12))
        stock.add_item(Chilipepper(5))
        self.assertEqual([5, 12, 4, 3], giveListofstock(
            stock.chilipepperList, type))

        stock.pop_item('honing', 4)
        self.assertEqual([2, 3, 10], giveListofstock(stock.honeyList, type))

        stock.pop_item('chilipeper', 3)
        self.assertEqual([4, 5, 12], giveListofstock(
            stock.chilipepperList, type))

        stock.add_item(Chilipepper(8))
        stock.add_item(Chilipepper(13))
        stock.add_item(Chilipepper(35))
        stock.add_item(Chilipepper(1))
        stock.pop_item('chilipeper', 10)
        self.assertEqual([1, 4, 5, 8, 13, 35], giveListofstock(
            stock.chilipepperList, type))

    def testCleanStock(self, type='cll'):
        stock = Stock(type)
        stock.add_item(Chilipepper(1))
        stock.add_item(Chilipepper(10))
        stock.add_item(Chilipepper(12))
        stock.add_item(Chilipepper(78))
        ##
        stock.add_item(Honey(13))
        stock.add_item(Honey(23))
        stock.add_item(Honey(4))
        stock.add_item(Honey(18))
        ##
        stock.add_item(Marshmallow(16))
        stock.add_item(Marshmallow(21))
        stock.add_item(Marshmallow(32))
        stock.add_item(Marshmallow(11))
        ##
        stock.add_item(Chocolateshot(8, "bruin"))
        stock.add_item(Chocolateshot(9, "bruin"))
        stock.add_item(Chocolateshot(10, "bruin"))
        stock.add_item(Chocolateshot(11, "bruin"))
        ##
        stock.add_item(Chocolateshot(11, "wit"))
        stock.add_item(Chocolateshot(10, "wit"))
        stock.add_item(Chocolateshot(9, "wit"))
        stock.add_item(Chocolateshot(8, "wit"))
        ##
        stock.add_item(Chocolateshot(54, "melk"))
        stock.add_item(Chocolateshot(54, "melk"))
        stock.add_item(Chocolateshot(1, "melk"))
        stock.add_item(Chocolateshot(54, "melk"))
        ##
        stock.clean_stock(10)

        self.assertEqual([10, 12, 78], giveListofstock(
            stock.chilipepperList, type))
        self.assertEqual([13, 18, 23], giveListofstock(stock.honeyList, type))
        self.assertEqual([11, 16, 21, 32], giveListofstock(
            stock.marshmallowList, type))
        self.assertEqual([10, 11], giveListofstock(
            stock.brownChocolateList, type))
        self.assertEqual([10, 11], giveListofstock(
            stock.whiteChocolateList, type))
        self.assertEqual([54, 54, 54], giveListofstock(
            stock.milkChocolateList, type))
