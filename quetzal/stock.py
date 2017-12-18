from datastructures import *
from product import *

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
            self.blackChocolateList = CircularLinkedList()
        elif "cll" == type or type == "CLL":
            self.type = "cll"
            self.honeyList = CircularLinkedList()
            self.marshmallowList = CircularLinkedList()
            self.chilipepperList = CircularLinkedList()
            self.whiteChocolateList = CircularLinkedList()
            self.brownChocolateList = CircularLinkedList()
            self.milkChocolateList = CircularLinkedList()
            self.blackChocolateList = CircularLinkedList()

    def add_item(self, item):
        """
        Adds an item, which is a certain product, to the corresponding table.

        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  'item' has been added to the corresponding list, if it's type was correct. In his case, True
                is returned. If the it's type was incorrect, False is returned.
        """
        index = 1

        if isinstance(item, Honing):
            self.honeyList.insert(index, item)
        elif isinstance(item, Chilipeper):
            self.chilipepperList.insert(index, item)
        elif isinstance(item, Marshmallow):
            self.marshmallowList.insert(index, item)
        elif isinstance(item, Chocoladeshot):
            if item.getName() == "wit":
                self.whiteChocolateList.insert(index, item)
            elif item.getName() == "bruin":
                self.brownChocolateList.insert(index, item)
            elif item.getName() == "melk":
                self.milkChocolateList.insert(index, item)
            else:
                self.blackChocolateList.insert(index, item)
        else:
            return False
        return True

    def is_empty(self, product):
        """
        Checks whether the table of the given product is empty or not.

        PRE  :  'product' is a string corresponding to the item-type of a list in the stock. (Marshmallow, Honey, Chilipepper,
                WhiteChocolate, MilkChocolate or BrownChocolate).
        POST :  If the corresponding list is empty, True will be returned.
        """
        if product == "Honing" or product == "honing":
            return self.honeyList.isEmpty()
        elif product == "chilipeper" or product == "chili peper" or product == "Chilipeper" or product == "Chili peper":
            return self.chilipepperList.isEmpty()
        elif product == "Witte chocolade" or product == "wit" or product == "Wit" or product == "witte chocolate":
            return self.whiteChocolateList.isEmpty()
        elif product == "Bruine chocolade" or product == "Bruine" or product == "bruine" or product == "bruine chocolade":
            return self.brownChocolateList.isEmpty()
        elif product == "Melk chocolade" or product == "Melk" or product =="melk" or product == "melk chocolade":
            return self.milkChocolateList.isEmpty()
        elif product == "Zwarte chocolade" or product == "Zwart" or product =="zwart" or product == "zwarte chocolade":
            return self.blackChocolateList.isEmpty()
        elif product == "marshmallow" or product == "Marshmallow":
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
        if soort == Honey or soort == Marshmallow or soort == WhiteChocolate or soort == BrownChocolate or soort == MilkChocolate or soort == Chilipepper:
            return True
        return False

    def find_type(self, item):
        """
        Finds the type of 'item'.
        PRE  :  'item' is an object of type Marshmellow, Chilipepper, Honey, WhiteChocolate, MilkChocolate or BrownChocolate)
        POST :  The type is returned, this type corresponds to the class of 'item'.
        """
        return type(item)

    def get_size(self, item):
        """
        Finds the size of the list that contains 'item' types.
        :param item: Determines the type of product. (Marshmallow, chili peper, honing...)
        :return: an integer that represents the size of the table that contains 'item' products
        PRE :   'item' is a string that corresponds to one of the products.
        POST:   The size of the table that contains 'item' products is returned.
        """
        if item == "Honing" or item == "honing":
            return self.honeyList.getLength()
        if item == "marshmallow" or item == "Marshmallow":
            return self.marshmallowList.getLength()
        if item == "wit" or item == "Wit" or item == "Witte chocolade" or item == "witte chocolade":
            return self.whiteChocolateList.getLength()
        if item == "bruin" or item == "Bruin" or item == "bruine chocolade" or item == "Bruine Chocolade":
            return self.brownChocolateList.getLength()
        if item == "zwart" or item == "Zwart" or item == "Zwarte chocolade" or item == "zwart chocolade":
            return self.blackChocolateList.getLength()
        if item == "melk" or item == "Melk" or item == "Melk chocolade" or item == "melk chocolade":
            return self.milkChocolateList.getLength()
        if item == "chili peper" or item == "chilipeper" or item == "Chilipeper" or item == "Chili peper":
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

    def pop_item(self, product, date):
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
        if product == "Honing" or product == "honing":
            return self.remove_by_date(self.honeyList, date)
        elif product == "chilipeper" or product == "chili peper" or product == "Chilipeper" or product == "Chili peper":
            return self.remove_by_date(self.chilipepperList, date)
        elif product == "Witte chocolade" or product == "wit" or product == "Wit" or product == "witte chocolate":
            return self.remove_by_date(self.whiteChocolateList, date)
        elif product == "Bruine chocolade" or product == "Bruine" or product == "bruine" or product == "bruine chocolade":
            return self.remove_by_date(self.brownChocolateList, date)
        elif product == "Melk chocolade" or product == "Melk" or product == "melk" or product == "melk chocolade":
            return self.remove_by_date(self.milkChocolateList, date)
        elif product == "Zwarte chocolade" or product == "Zwart" or product == "zwart" or product == "zwarte chocolade":
            return self.remove_by_date(self.blackChocolateList, date)
        elif product == "marshmallow" or product == "Marshmallow":
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

                        if place_after.get_expiration_date < place_i.get_expiration_date:
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
                        if place_after.get_expiration_date < place_i.get_expiration_date:
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
            if item_at_index.get_expiration_date >= date:
                stockList.delete(index)
                return True
            index += 1
        return False