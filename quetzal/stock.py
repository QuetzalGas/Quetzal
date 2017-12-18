from Double_Linked_Lists import Double_Linked_List
from CircularLinkedList import CircularLinkedList
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Title:      Stock
creator:    Joke Duwaerts
date:       December 2017
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- tabellen:
    * chocoladeshots ==> 3 soorten: melk, wit, bruin
    * honing
    * chilipeper
    * marshwallow
    * chocolademelk
- init -> 4 lege tabellen
- addItem( item, bool )
- popItem( item )
- contains( item, bool )
- findType( item, type )
- isEmpty( type, bool )
- cleanStock( list vervallen )
"""

class Product:
    def __init__(self, vervaldatum):
        self.prijs = 0
        self.vervaldatum = vervaldatum

class Chilipepper(Product):
    def __init__(self, vervaldatum):
        Product.__init__(self, vervaldatum)

class Chocolateshots(Product):
    def __init__(self, vervaldatum):
        Product.__init__(self, vervaldatum)

class MilkChocolate(Chocolateshots):
    def __init__(self, vervaldatum):
        Chocolateshots.__init__(self, vervaldatum)

class BrownChocolate(Chocolateshots):
    def __init__(self, vervaldatum):
        Chocolateshots.__init__(self, vervaldatum)

class WhiteChocolate(Chocolateshots):
    def __init__(self, vervaldatum):
        Chocolateshots.__init__(self, vervaldatum)

class Honey(Product):
    def __init__(self, vervaldatum):
        Product.__init__(self, vervaldatum)

class Marshmallow(Product):
    def __init__(self, vervaldatum):
        Product.__init__(self, vervaldatum)

class Stock:
    def __init__(self, type):
        """
        Creates empty lists for the products: honey, marshmallows, chili pepper and chocolate shots (white, brown and
        milk chocolate).

        PRE  :  Type is a circular linked list (CLL) or a double linked list (DLL). Type decides the kind of implemen-
                tation of the stocks.
        POST :  The stock now contains six empty lists.
        """

        if "dll" == type or type == "DLL":
            self.type = "dll"
            self.honeyList = Double_Linked_List()
            self.marshmallowList = Double_Linked_List()
            self.chilipepperList = Double_Linked_List()
            self.whiteChocolateList = Double_Linked_List()
            self.brownChocolateList = Double_Linked_List()
            self.milkChocolateList = Double_Linked_List()
        elif "cll" == type or type == "CLL":
            self.type = "cll"
            self.honeyList = CircularLinkedList()
            self.marshmallowList = CircularLinkedList()
            self.chilipepperList = CircularLinkedList()
            self.whiteChocolateList = CircularLinkedList()
            self.brownChocolateList = CircularLinkedList()
            self.milkChocolateList = CircularLinkedList()

    def addItem(self, item):
        """
        Adds an item, which is a certain product, to the corresponding table.

        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  'item' has been added to the corresponding list, if it's type was correct. In his case, True
                is returned. If the it's type was incorrect, False is returned.
        """
        index = 1

        if isinstance(item, Honey):
            self.honeyList.insert(index, item)
        elif isinstance(item, Chilipepper):
            self.chilipepperList.insert(index, item)
        elif isinstance(item, Marshmallow):
            self.marshmallowList.insert(index, item)
        elif isinstance(item, WhiteChocolate):
            self.whiteChocolateList.insert(index, item)
        elif isinstance(item, BrownChocolate):
            self.brownChocolateList.insert(index, item)
        elif isinstance(item, MilkChocolate):
            self.milkChocolateList.insert(index, item)
        else:
            return False
        return True

    def popItem(self, itemType, date):
        """
        Removes the product (of type 'itemType') with the most urgent expiry date from te corresponding stock-list.
        Product with expiry dates that have already passed will be ignored, the method 'cleanStock' takes
        care of removing those.

        PRE  :  'itemType' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If 'itemType' corresponds to a type of the lists in the stock and this particular list containes items
                with expiry dates "higher or equal to" the given expiry date, then the item with the most urgent expiry
                date is removed from that list. In this case, True is returned.
        """
        if itemType == "Honey" or itemType == "honey":
            return self.removeByDate(self.honeyList, date)
        elif "marshmallow" == itemType or itemType == "Marshmallow":
            return self.removeByDate(self.marshmallowList, date)
        elif itemType == "chilipepper" or itemType == "chili pepper" or itemType == "Chilipepper" or itemType == "Chili pepper":
            return self.removeByDate(self.chilipepperList, date)
        elif itemType == "White chocolate" or itemType == "WhiteChocolate" or itemType == "white chocolate" or itemType == "whitechocolate":
            return self.removeByDate(self.whiteChocolateList, date)
        elif itemType == "Brown chocolate" or itemType == "BrownChocolate" or itemType == "brown chocolate" or itemType == "bhitechocolate":
            return self.removeByDate(self.brownChocolateList, date)
        elif itemType == "Milk chocolate" or itemType == "MilkChocolate" or itemType == "milk chocolate" or itemType == "milkchocolate":
            return self.removeByDate(self.milkChocolateList, date)
        else:
            print("\tUnvalid product type.")
            return False

    def isEmpty(self, product):
        """
        Checks whether the table of the given product is empty or not.

        PRE  :  'product' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If the corresponding list is empty, True will be returned.
        """
        if product == "Honey" or product == "honey":
            return self.honeyList.isEmpty()
        elif product == "chilipepper" or product == "chili pepper" or product == "Chilipepper" or product == "Chili pepper":
            return self.chilipepperList.isEmpty()
        elif product == "White chocolate" or product == "WhiteChocolate" or product == "white chocolate" or product == "whitechocolate":
            return self.whiteChocolateList.isEmpty()
        elif product == "Brown chocolate" or product == "BrownChocolate" or product == "brown chocolate" or product == "bhitechocolate":
            return self.brownChocolateList.isEmpty()
        elif product == "Milk chocolate" or product == "MilkChocolate" or product =="milk chocolate" or product == "milkchocolate":
            return self.milkChocolateList.isEmpty()
        elif product == "marshmallow" or product == "Marshmallow":
            return self.marshmallowList.isEmpty()
        else:
            print("\tUnvalid product type.")
            return False

    def containsItem(self, item):
        """
        Checks whether a list of type('item') is present.

        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  True is returned, if there is a list that contains items of type('item')
        """
        soort = type(item)
        if soort == Honey or soort == Marshmallow or soort == WhiteChocolate or soort == BrownChocolate or soort == MilkChocolate or soort == Chilipepper:
            return True
        return False

    def findType(self, item):
        """
        Finds the type of 'item'.
        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  The type is returned, this type corresponds to the class of 'item'.
        """
        return type(item)

    def cleanStock(self, date):
        """
        Checks all stock-lists and returns a list which contains products that are expired.

        PRE  :  Date is the current Date, used to check which expiry dates have already passed.
        POST :  A list of expired products will be returned.
        """
        allDeletedItems = list()
        allDeletedItems += self.cleanOneStock(self.honeyList, date)
        allDeletedItems += self.cleanOneStock(self.whiteChocolateList, date)
        allDeletedItems += self.cleanOneStock(self.brownChocolateList, date)
        allDeletedItems += self.cleanOneStock(self.milkChocolateList, date)
        allDeletedItems += self.cleanOneStock(self.chilipepperList, date)
        allDeletedItems += self.cleanOneStock(self.marshmallowList, date)
        return allDeletedItems

    def sort(self, stockList):
        """
        Sorts the items in a 'stockList' by means of their searchkey (expiry date).
        The bubble sort is used.
        """
        sorted = False
        if self.type == "cll":
            for area in range(1, stockList.getLength()):
                if not sorted:
                    sorted = True
                    for i in range(1, stockList.getLength() - area + 1):
                        (place_i, bool) = stockList.retrieve(i)
                        (place_after, bool) = stockList.retrieve(i + 1)

                        if place_i.vervaldatum > place_after.vervaldatum:
                            sorted = False

                            stockList.insert(i, place_after)
                            stockList.delete(i + 2)

        else:
            for area in range(1, stockList.getLength()):
                if not sorted:
                    sorted = True
                    for i in range(1, stockList.getLength() - area + 1):
                        place_i = stockList.searchNode(i)
                        place_after = place_i.next

                        if place_i.item.vervaldatum > place_after.item.vervaldatum:
                            sorted = False
                            if place_i.prev is not None:
                                place_i.prev.next = place_after
                            place_after.prev = place_i.prev
                            place_i.prev = place_after
                            place_i.next = place_after.next
                            place_after.next = place_i
                            if place_i.next is not None:
                                place_i.next.prev = place_i
                            if (i == 1):
                                stockList.head = place_after

    def removeByDate(self, stockList, date):
        """
        Removes the item with most urgent expiry date from the given 'stockList' (one of the six lists that the stock
        contains).

        PRE  :  'date' is the date that is used as reference to check which expiry dates have already passed and must
                therefore be ignored. (One does not simply put an expired product into a chocolate milk.)
                'stockList' is one of the six stock-lists that the whole stock contains.
        POST :  The item with most urgent expiry date is removed from 'stockList' and True is returned. If there wasn't
                an item with a expiry date "higher or equal" to 'date', then False is returned.
        """
        if stockList.isEmpty():
            return False
        self.sort(stockList)
        if self.type == "cll":
            prev = stockList.head
            cur = prev.next
            while cur is not stockList.dummyhead:
                if cur.item.vervaldatum >= date:
                    prev.next = cur.next
                    return True
                cur = cur.next
                prev = prev.next
        else:
            cur = stockList.head
            while cur.next is not None:
                if cur.item.vervaldatum >= date:
                    if cur.prev is not None:
                        cur.prev.next = cur.next
                    else:
                        stockList.head = cur.next
                    cur.next.prev = cur.prev
                    stockList.length -= 1
                    return True
                cur = cur.next
        return False

    def cleanOneStock(self, stockList, date):
        """
        Cleans 'stockList' by removing all items (if present) with an expiry date that has already passed 'date'.
        PRE  :  'stockList' is one of the stocks of the whole stock.
        POST :  All expired items (expiry date < 'date') are removed from the 'stockList'. A list containing the
                removed items is returned. (the list is empty when no items were returned)
        """
        deletedItems = list()
        self.sort(stockList)

        index = 1
        if self.type == 'cll':
            first = stockList.retrieve(index)[0]
        else:
            first = stockList.searchItem(index)[0]
        if first is None:
            return deletedItems
        while first.vervaldatum < date and stockList.getLength() >= 1:
            deletedItems.append(first.vervaldatum)
            stockList.delete(index)
            if self.type == "cll":
                first = stockList.retrieve(index)[0]
            else:
                first = stockList.searchItem(index)[0]
            if first is None:
                break
        return deletedItems

    def popItem2(self, itemType, date):
        """
        Removes the product (of type 'itemType') with the most urgent expiry date from te corresponding stock-list.
        Product with expiry dates that have already passed will be ignored, the method 'cleanStock' takes
        care of removing those.

        PRE  :  'itemType' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If 'itemType' corresponds to a type of the lists in the stock and this particular list containes items
                with expiry dates "higher or equal to" the given expiry date, then the item with the most urgent expiry
                date is removed from that list. In this case, True is returned.
        """
        if itemType == "Honey" or itemType == "honey":
            return self.removeByDate2(self.honeyList, date)
        elif "marshmallow" == itemType or itemType == "Marshmallow":
            return self.removeByDate2(self.marshmallowList, date)
        elif itemType == "chilipepper" or itemType == "chili pepper" or itemType == "Chilipepper" or itemType == "Chili pepper":
            return self.removeByDate2(self.chilipepperList, date)
        elif itemType == "White chocolate" or itemType == "WhiteChocolate" or itemType == "white chocolate" or itemType == "whitechocolate":
            return self.removeByDate2(self.whiteChocolateList, date)
        elif itemType == "Brown chocolate" or itemType == "BrownChocolate" or itemType == "brown chocolate" or itemType == "bhitechocolate":
            return self.removeByDate2(self.brownChocolateList, date)
        elif itemType == "Milk chocolate" or itemType == "MilkChocolate" or itemType == "milk chocolate" or itemType == "milkchocolate":
            return self.removeByDate2(self.milkChocolateList, date)
        else:
            print("\tUnvalid product type.")
            return False

    def sort2(self, stockList):
        sorted = False
        if self.type == "cll":
            for area in range(1, stockList.getLength()):
                if not sorted:
                    sorted = True
                    for i in range(1, stockList.getLength() - area + 1):
                        (place_i, bool) = stockList.retrieve(i)
                        (place_after, bool) = stockList.retrieve(i + 1)

                        if place_i.vervaldatum > place_after.vervaldatum:
                            sorted = False

                            stockList.insert(i, place_after)
                            stockList.delete(i + 2)

        else:
            for area in range(1, stockList.getLength()):
                if not sorted:
                    sorted = True
                    for i in range(0, stockList.getLength() - area + 1):
                        place_i = stockList.searchItem(i)[0]
                        place_after = stockList.searchItem(i+1)[0]
                        if not stockList.isEmpty():
                            cur = stockList.head
                            for j in range(0, stockList.getLength()):
                                cur = cur.next
                        if place_i.vervaldatum > place_after.vervaldatum:
                            sorted = False
                            stockList.delete(i+1)
                            stockList.insert(i, place_after)

    def removeByDate2(self, stockList, date):
        """
        Removes the item with most urgent expiry date from the given 'stockList' (one of the six lists that the stock
        contains).

        PRE  :  'date' is the date that is used as reference to check which expiry dates have already passed and must
                therefore be ignored. (One does not simply put an expired product into a chocolatemilk)
                'stockList' is one of the six stock-lists that the whole stock contains.
        POST :  The item with most urgent expiry date is removed from 'stockList' and True is returned. If there wasn't
                an item with a expiry date "higher or equal" to 'date', then False is returned.
        """
        if stockList.isEmpty():
            return False
        self.sort2(stockList)
        index = 0
        if self.type == 'cll':
            index = 1
        for i in range(0, stockList.getLength()):
            item_at_index = None
            if self.type == 'cll':
                item_at_index = stockList.retrieve(index)[0]
            else:
                item_at_index = stockList.searchItem(index)[0]
            if item_at_index.vervaldatum >= date:
                stockList.delete(index)
                return True
            index += 1
        return False

    def cleanStock2(self, date):
        """
        Checks all stock-lists and returns a list which contains products that are expired.

        PRE  :  Date is the current Date, used to check which expiry dates have already passed.
        POST :  A list of expired products will be returned.
        """
        allDeletedItems = list()
        allDeletedItems += self.cleanOneStock2(self.honeyList, date)
        allDeletedItems += self.cleanOneStock2(self.whiteChocolateList, date)
        allDeletedItems += self.cleanOneStock2(self.brownChocolateList, date)
        allDeletedItems += self.cleanOneStock2(self.milkChocolateList, date)
        allDeletedItems += self.cleanOneStock2(self.chilipepperList, date)
        allDeletedItems += self.cleanOneStock2(self.marshmallowList, date)
        return allDeletedItems

    def cleanOneStock2(self, stockList, date):
        """
        Cleans 'stockList' by removing all items (if present) with an expiry date that has already passed 'date'.
        PRE  :  'stockList' is one of the stocks of the whole stock.
        POST :  All expired items (expiry date < 'date') are removed from the 'stockList'. A list containing the
                removed items is returned. (the list is empty when no items were returned)
        """
        deletedItems = list()
        self.sort(stockList)

        index = 1
        if self.type == 'cll':
            first = stockList.retrieve(index)[0]
        else:
            first = stockList.searchItem(index)[0]
        if first is None:
            return deletedItems
        while first.vervaldatum < date and stockList.getLength() >= 1:
            deletedItems.append(first.vervaldatum)
            stockList.delete(index)
            if self.type == "cll":
                first = stockList.retrieve(index)[0]
            else:
                first = stockList.searchItem(index)[0]
            if first is None:
                break
        return deletedItems

def printStocks(stock, type):
    print("\n===========================================================")
    print(" Honey list :")
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
    print("\n===========================================================")

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