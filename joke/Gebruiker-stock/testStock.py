# Tests of class Stock
# by Joke Duwaerts

from Stock import Stock, Chilipepper, MilkChocolate, BrownChocolate, WhiteChocolate, Honey, Marshmallow, Double_Linked_List
from unittest import TestCase

def printStocks(stock, type):
    print("\n\t Honey list :")
    printList(stock.honeyList, type)
    print("\n\t Marshmallow list :")
    printList(stock.marshmallowList, type)
    print("\n\t Chilipepper list :")
    printList(stock.chilipepperList, type)
    print("\n\t Milk chocolate list :")
    printList(stock.milkChocolateList, type)
    print("\n\t Brown chocolate list :")
    printList(stock.brownChocolateList, type)
    print("\n\t White chocolate list :")
    printList(stock.whiteChocolateList, type)

def printList(listy, type):
    if type == 'cll':
        if not listy.isEmpty():
            cur = listy.head
            while cur.next is not listy.dummyhead:
                cur = cur.next
                print(cur.item.vervaldatum, " ",  end="")
    else:
        if not listy.isEmpty():
            cur = listy.head
            for i in range(0, listy.getLength()):
                print(cur.item.vervaldatum, " ", end="")
                cur = cur.next

def giveListofstock(listy, type):
    myList = list()
    if type == 'cll':
        if not listy.isEmpty():
            cur = listy.head
            while cur.next is not listy.dummyhead:
                cur = cur.next
                myList.append(cur.item.vervaldatum)
    else:
        if not listy.isEmpty():
            cur = listy.head
            for i in range(0, listy.getLength()):
                myList.append(cur.item.vervaldatum)
                cur = cur.next
    return myList

class testStock(TestCase):
    def testEmptyBeforeAdding(self, type = 'cll'):
        stock = Stock(type)
        self.assertTrue(stock.isEmpty("chili pepper"))
        self.assertTrue(stock.isEmpty("honey"))
        self.assertTrue(stock.isEmpty("White chocolate"))
        self.assertTrue(stock.isEmpty("Milk chocolate"))
        self.assertTrue(stock.isEmpty("BrownChocolate"))
        self.assertTrue(stock.isEmpty("marshmallow"))

    def testEmptyAfterAdding(self, type='cll'):
        stock = Stock(type)
        stock.addItem(WhiteChocolate(2))
        stock.addItem(Marshmallow(3))
        stock.addItem(Honey(2))
        stock.addItem(Chilipepper(12))
        stock.addItem(BrownChocolate(52))
        stock.addItem(MilkChocolate(753))

        self.assertFalse(stock.isEmpty("chili pepper"))
        self.assertFalse(stock.isEmpty("honey"))
        self.assertFalse(stock.isEmpty("White chocolate"))
        self.assertFalse(stock.isEmpty("Milk chocolate"))
        self.assertFalse(stock.isEmpty("BrownChocolate"))
        self.assertFalse(stock.isEmpty("marshmallow"))

    def testContainsItem(self, type='dll'):
        stock = Stock(type)
        self.assertFalse(stock.containsItem(55))
        self.assertFalse(stock.containsItem("Pan Galactic Gargle Blaster"))
        self.assertTrue(stock.containsItem(WhiteChocolate(2)))
        self.assertTrue(stock.containsItem(Marshmallow(3)))
        self.assertTrue(stock.containsItem(Honey(2)))
        self.assertTrue(stock.containsItem(BrownChocolate(5)))
        self.assertTrue(stock.containsItem(MilkChocolate(3)))
        self.assertTrue(stock.containsItem(Chilipepper(2)))

    def testAddAndPop(self, type='cll'):
        stock = Stock(type)
        stock.addItem(Honey(2))
        stock.addItem(Honey(4))
        stock.addItem(Honey(10))
        stock.addItem(Honey(3))
        self.assertEqual([3,10,4,2], giveListofstock(stock.honeyList, type))

        stock.addItem(Chilipepper(3))
        stock.addItem(Chilipepper(4))
        stock.addItem(Chilipepper(12))
        stock.addItem(Chilipepper(5))
        self.assertEqual([5,12,4,3], giveListofstock(stock.chilipepperList, type))

        stock.popItem('honey', 4)
        self.assertEqual([2,3,10], giveListofstock(stock.honeyList, type))

        stock.popItem('chilipepper', 3)
        self.assertEqual([4,5,12], giveListofstock(stock.chilipepperList, type))

        stock.addItem(Chilipepper(8))
        stock.addItem(Chilipepper(13))
        stock.addItem(Chilipepper(35))
        stock.addItem(Chilipepper(1))
        stock.popItem('chilipepper', 10)
        self.assertEqual([1,4,5,8,13,35], giveListofstock(stock.chilipepperList, type))

    def testCleanStock(self, type='cll'):
        stock = Stock(type)
        stock.addItem(Chilipepper(1))
        stock.addItem(Chilipepper(10))
        stock.addItem(Chilipepper(12))
        stock.addItem(Chilipepper(78))
        ##
        stock.addItem(Honey(13))
        stock.addItem(Honey(23))
        stock.addItem(Honey(4))
        stock.addItem(Honey(18))
        ##
        stock.addItem(Marshmallow(16))
        stock.addItem(Marshmallow(21))
        stock.addItem(Marshmallow(32))
        stock.addItem(Marshmallow(11))
        ##
        stock.addItem(BrownChocolate(8))
        stock.addItem(BrownChocolate(9))
        stock.addItem(BrownChocolate(10))
        stock.addItem(BrownChocolate(11))
        ##
        stock.addItem(WhiteChocolate(11))
        stock.addItem(WhiteChocolate(10))
        stock.addItem(WhiteChocolate(9))
        stock.addItem(WhiteChocolate(8))
        ##
        stock.addItem(MilkChocolate(54))
        stock.addItem(MilkChocolate(54))
        stock.addItem(MilkChocolate(1))
        stock.addItem(MilkChocolate(54))
        ##
        stock.cleanStock(10)

        self.assertEqual([10,12,78], giveListofstock(stock.chilipepperList, type))
        self.assertEqual([13,18,23], giveListofstock(stock.honeyList, type))
        self.assertEqual([11,16,21,32], giveListofstock(stock.marshmallowList, type))
        self.assertEqual([10,11], giveListofstock(stock.brownChocolateList, type))
        self.assertEqual([10,11], giveListofstock(stock.whiteChocolateList, type))
        self.assertEqual([54,54,54], giveListofstock(stock.milkChocolateList, type))