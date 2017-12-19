from .datastructures import *
from .product import *
from unittest import TestCase

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
            self.honeyList = AdtDoublyLinkedList()
            self.marshmallowList = AdtDoublyLinkedList()
            self.chilipepperList = AdtDoublyLinkedList()
            self.whiteChocolateList = AdtDoublyLinkedList()
            self.brownChocolateList = AdtDoublyLinkedList()
            self.milkChocolateList = AdtDoublyLinkedList()
            self.blackChocolateList = AdtDoublyLinkedList()
        elif "cll" == type or type == "CLL":
            self.type = "cll"
            self.honeyList = AdtCircularLinkedList()
            self.marshmallowList = AdtCircularLinkedList()
            self.chilipepperList = AdtCircularLinkedList()
            self.whiteChocolateList = AdtCircularLinkedList()
            self.brownChocolateList = AdtCircularLinkedList()
            self.milkChocolateList = AdtCircularLinkedList()
            self.blackChocolateList = AdtCircularLinkedList()

    def add_item(self, item):
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
        elif isinstance(item, Chocolateshot):
            if item.get_name() == "wit":
                self.whiteChocolateList.insert(index, item)
            elif item.get_name() == "bruin":
                self.brownChocolateList.insert(index, item)
            elif item.get_name() == "melk":
                self.milkChocolateList.insert(index, item)
            else:
                self.blackChocolateList.insert(index, item)
        else:
            return False
        return True

    def is_empty(self, product_type):
        """
        Checks whether the table of the given product_type is empty or not.

        PRE  :  'product_type' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If the corresponding list is empty, True will be returned.
        """
        if product_type == "honing" or product_type == "honey":
            return self.honeyList.isEmpty()
        elif product_type == "chilipeper" or product_type == "chili pepper" or product_type == "chilipepper":
            return self.chilipepperList.isEmpty()
        elif product_type == "witte chocolade" or product_type == "wit" or product_type == "white" or product_type == "white chocolate":
            return self.whiteChocolateList.isEmpty()
        elif product_type == "brown chocolate" or product_type == "brown" or product_type == "bruine" or product_type == "bruine chocolade":
            return self.brownChocolateList.isEmpty()
        elif product_type == "milk chocolate" or product_type == "milk" or product_type =="melk" or product_type == "melk chocolade":
            return self.milkChocolateList.isEmpty()
        elif product_type == "black chocolade" or product_type == "black" or product_type =="zwart" or product_type == "zwarte chocolade":
            return self.blackChocolateList.isEmpty()
        elif product_type == "marshmallow" or product_type == "Marshmallow":
            return self.marshmallowList.isEmpty()
        else:
            print("\tUnvalid product type.")
            return False

    def contains_item(self, item):
        """
        Checks whether a list of type('item') is present.

        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  True is returned, if there is a list that contains items of type('item')
        """
        soort = type(item)
        if soort == Honey or soort == Marshmallow or soort == Chocolateshot or soort == Chilipepper:
            return True
        return False

    def find_type(self, item):
        """
        Finds the type of 'item'.
        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  The type is returned, this type corresponds to the class of 'item'.
        """
        return type(item)

    def get_size(self, product_type):
        """
        Finds the size of the list that contains 'item' types.
        :param item: Determines the type of product. (Marshmallow, chili peper, honing...)
        :return: an integer that represents the size of the table that contains 'item' products
        PRE :   'item' is a string that corresponds to one of the products.
        POST:   The size of the table that contains 'item' products is returned.
        """
        if product_type == "honing" or product_type == "honey":
            return self.honeyList.getLength()
        elif product_type == "marshmallow" or product_type == "Marshmallow":
            return self.marshmallowList.getLength()
        elif product_type == "witte chocolade" or product_type == "wit" or product_type == "white" or product_type == "white chocolate":
            return self.whiteChocolateList.getLength()
        elif product_type == "brown chocolate" or product_type == "brown" or product_type == "bruine" or product_type == "bruine chocolade":
            return self.brownChocolateList.getLength()
        elif product_type == "black chocolade" or product_type == "black" or product_type =="zwart" or product_type == "zwarte chocolade":
            return self.blackChocolateList.getLength()
        elif product_type == "milk chocolate" or product_type == "milk" or product_type =="melk" or product_type == "melk chocolade":
            return self.milkChocolateList.getLength()
        elif product_type == "chilipeper" or product_type == "chili pepper" or product_type == "chilipepper":
            return self.chilipepperList.getLength()
        else:
            print("Unvalid type.")
            return None

    def clean_stock(self, date):
        """
        Checks all stock-lists and returns a list which contains products that are expired.

        PRE  :  Date is the current Date, used to check which expiry dates have already passed.
        POST :  A list of expired products will be returned.
        """
        allDeletedItems = list()
        allDeletedItems += self.clean_one_stock(self.honeyList, date)
        allDeletedItems += self.clean_one_stock(self.whiteChocolateList, date)
        allDeletedItems += self.clean_one_stock(self.brownChocolateList, date)
        allDeletedItems += self.clean_one_stock(self.milkChocolateList, date)
        allDeletedItems += self.clean_one_stock(self.chilipepperList, date)
        allDeletedItems += self.clean_one_stock(self.marshmallowList, date)
        allDeletedItems += self.clean_one_stock(self.blackChocolateList, date)
        return allDeletedItems

    def clean_one_stock(self, stockList, date):
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
        while first.get_expiration_date() < date and stockList.getLength() >= 1:
            deletedItems.append(first.get_expiration_date())
            stockList.delete(index)
            if self.type == "cll":
                first = stockList.retrieve(index)[0]
            else:
                first = stockList.searchItem(index)[0]
            if first is None:
                break
        return deletedItems

    def pop_item(self, product_type, date):
        """
        Removes the product (of type 'product_type') with the most urgent expiry date from te corresponding stock-list.
        Product with expiry dates that have already passed will be ignored, the method 'clean_stock' takes
        care of removing those.

        PRE  :  'product_type' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If 'product_type corresponds to a type of the lists in the stock and this particular list containes items
                with expiry dates "higher or equal to" the given expiry date, then the item with the most urgent expiry
                date is removed from that list. In this case, True is returned.
        """
        if product_type == "honing" or product_type == "honey":
            return self.remove_by_date(self.honeyList, date)
        elif product_type == "chilipeper" or product_type == "chili pepper" or product_type == "chilipepper":
            return self.remove_by_date(self.chilipepperList, date)
        elif product_type == "witte chocolade" or product_type == "wit" or product_type == "white" or product_type == "white chocolate":
            return self.remove_by_date(self.whiteChocolateList, date)
        elif product_type == "brown chocolate" or product_type == "brown" or product_type == "bruin" or product_type == "bruine chocolade":
            return self.remove_by_date(self.brownChocolateList, date)
        elif product_type == "milk chocolate" or product_type == "milk" or product_type == "melk" or product_type == "melk chocolade":
            return self.remove_by_date(self.milkChocolateList, date)
        elif product_type == "black chocolade" or product_type == "black" or product_type == "zwart" or product_type == "zwarte chocolade":
            return self.remove_by_date(self.blackChocolateList, date)
        elif product_type == "marshmallow" or product_type == "Marshmallow":
            return self.remove_by_date(self.marshmallowList, date)
        else:
            print("\tUnvalid product type.")
            return False

    def sort(self, stockList):
        sorted = False
        if self.type == "cll":
            for area in range(1, stockList.getLength()):
                if not sorted:
                    sorted = True
                    for i in range(1, stockList.getLength() - area + 1):
                        (place_i, bool) = stockList.retrieve(i)
                        (place_after, bool) = stockList.retrieve(i + 1)

                        if place_after.get_expiration_date() < place_i.get_expiration_date():
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
                        if place_after.get_expiration_date() < place_i.get_expiration_date():
                            sorted = False
                            stockList.delete(i+1)
                            stockList.insert(i, place_after)

    def remove_by_date(self, stockList, date):
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
        self.sort(stockList)
        index = 0
        if self.type == 'cll':
            index = 1
        for i in range(0, stockList.getLength()):
            if self.type == 'cll':
                item_at_index = stockList.retrieve(index)[0]
            else:
                item_at_index = stockList.searchItem(index)[0]
            if item_at_index.get_expiration_date() >= date:
                stockList.delete(index)
                return True
            index += 1
        return False
