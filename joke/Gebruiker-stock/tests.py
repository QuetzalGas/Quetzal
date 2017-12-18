# Tests of class Stock
# by Joke Duwaerts

from Stock import Stock, Chilipepper, MilkChocolate, BrownChocolate, WhiteChocolate, Honey, Marshmallow, Double_Linked_List
from unittest import TestCase

# # testing the sort algroritm of the CircularLinkedList
# def printList(listy):
#     if not listy.isEmpty():
#         cur = listy.head
#         while cur.next is not listy.dummyhead:
#             cur = cur.next
#             print(cur.item.vervaldatum)
#
# listy = CircularLinkedList()
# listy.insert(1, Marshmallow(12))
# listy.insert(1, Marshmallow(15))
# listy.insert(1, Marshmallow(22))
# listy.insert(1, Marshmallow(18))
# listy.insert(1, Marshmallow(2))
# printList(listy)
# listy.sort()
# printList(listy)
# listy.insert(2, Marshmallow(77))
# listy.insert(2, Marshmallow(0))
# listy.insert(2, Marshmallow(18))
# listy.insert(2, Marshmallow(33))
# listy.insert(2, Marshmallow(41))
# listy.sort()
# printList(listy)
#
# # testing the sort algoritm of the Double linked list
# def printListDOUBLE(listy):
#     if not listy.isEmpty():
#         cur = listy.head
#         for i in range(0, listy.getLength()):
#             print(cur.item.vervaldatum)
#             cur = cur.next
#
# listy = Double_Linked_List()
# listy.insert(1, Marshmallow(13))
# listy.insert(1, Marshmallow(15))
# listy.insert(1, Marshmallow(22))
# listy.insert(1, Marshmallow(18))
# listy.insert(1, Marshmallow(11))
# # printListDOUBLE(listy)
# # listy.sort()
# listy.insert(2, Marshmallow(77))
# listy.insert(2, Marshmallow(2))
# listy.insert(2, Marshmallow(18))
# listy.insert(2, Marshmallow(33))
# listy.insert(2, Marshmallow(41))
# printListDOUBLE(listy)
# listy.sort()
# printListDOUBLE(listy)

# chilipep1 = Chilipepper(1)
# chilipep2 = Chilipepper(2)
# chilipep3 = Chilipepper(3)
# chilipep4 = Chilipepper(4)
# chilipep5 = Chilipepper(5)
#
# marsh1 = Marshmallow(10)
# marsh2 = Marshmallow(11)
# marsh3 = Marshmallow(12)
# marsh4 = Marshmallow(13)
# marsh5 = Marshmallow(14)
#
# honey1 = Honey(20)
# honey2 = Honey(21)
# honey3 = Honey(22)
# honey4 = Honey(23)
# honey5 = Honey(24)
#
# white1 = WhiteChocolate(30)
# white2 = WhiteChocolate(31)
# white3 = WhiteChocolate(31)
# white4 = WhiteChocolate(31)
# white5 = WhiteChocolate(32)
#
# brown1 = BrownChocolate(40)
# brown2 = BrownChocolate(41)
# brown3 = BrownChocolate(42)
# brown4 = BrownChocolate(43)
# brown5 = BrownChocolate(44)
#
# milk1 = MilkChocolate(50)
# milk2 = MilkChocolate(51)
# milk3 = MilkChocolate(50)
# milk5 = MilkChocolate(50)
# milk4 = MilkChocolate(50)

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

# test = testStock()
# test.testEmptyBeforeAdding("cll")
# test.testEmptyAfterAdding("cll")
# test.testContainsItem("cll")
# test.testAddAndPop("cll")
# test.testCleanStock("cll")
#
# test1 = testStock()
# test1.testEmptyBeforeAdding("dll")
# test1.testEmptyAfterAdding("dll")
# test1.testContainsItem("dll")
# test1.testAddAndPop("dll")
# test1.testCleanStock("dll")

stock = Stock('dll')
stock.addItem(Honey(2))
stock.addItem(Honey(4))
stock.addItem(Honey(10))
stock.addItem(Honey(3))
stock.addItem(Honey(5))
printStocks(stock, 'dll')
# stock.sort2(stock.honeyList)
# printStocks(stock, 'cll')
stock.popItem2("honey", 3)
printStocks(stock, 'dll')

def printListy(listy):
    if not listy.isEmpty():
        cur = listy.head
        for i in range(0, listy.getLength()):
            print(cur.item, ", ", end="")
            cur = cur.next

#
# list = Double_Linked_List()
# list.insert(0, 5)
# list.insert(0, 3)
# list.insert(0, 12)
# list.insert(2, 7)
# printListy(list)
# print("\n jqsjfkqs:", list.searchItem(2)[0])
#
# list.delete(3)
# print("\n")
# printListy(list)

##########################################"
# stock = Stock('cll')
# stock.addItem(Chilipepper(1))
# stock.addItem(Chilipepper(10))
# stock.addItem(Chilipepper(12))
# stock.addItem(Chilipepper(78))
# stock.addItem(Chilipepper(15))
# stock.addItem(Chilipepper(17))
# ##
# stock.addItem(Honey(13))
# stock.addItem(Honey(23))
# stock.addItem(Honey(4))
# stock.addItem(Honey(18))
# ##
# stock.addItem(Marshmallow(16))
# stock.addItem(Marshmallow(21))
# stock.addItem(Marshmallow(32))
# stock.addItem(Marshmallow(11))
# stock.addItem(Marshmallow(11))
# stock.addItem(Marshmallow(15))
# ##
# stock.addItem(BrownChocolate(8))
# stock.addItem(BrownChocolate(9))
# stock.addItem(BrownChocolate(10))
# stock.addItem(BrownChocolate(11))
# ##
# stock.addItem(WhiteChocolate(11))
# stock.addItem(WhiteChocolate(10))
# stock.addItem(WhiteChocolate(9))
# stock.addItem(WhiteChocolate(8))
# ##
# stock.addItem(MilkChocolate(54))
# stock.addItem(MilkChocolate(54))
# stock.addItem(MilkChocolate(1))
# stock.addItem(MilkChocolate(54))
# printStocks(stock, 'cll')
# stock.popItem2("honey", 12)
# printStocks(stock, 'cll')
#
# stack = Stock('dll')
# stack.cleanStock(45)
# stack.popItem2("honey", 5)