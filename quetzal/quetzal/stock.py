from .datastructures import *
from .product import *
from .date import *
from unittest import TestCase

class Stock:
    def __init__(self, products, type):
        """ Creates empty lists for the given products.

        :param products list of the different products that need a stock

        PRE: Type is a circular linked list (CLL) or a doubly linked list (DLL). Type decides the kind of
        implementation of the stocks. Products are passed as a list of unique strings.
        POST: The stock contains as many lists as there are different products.
        """
        self.stocks = []
        for product in products:
            new_stock = type()
            new_stock[0] = Product(product, 0, 0, Date(0,0,0))
            self.stocks.append(new_stock)
        # TODO: raise ValueError("") voor type
        # TODO: datum van dummyproduct

    def add_item(self, item):
        """ Adds an item to the stock.

        If there is a stock that the item belongs in, the item will be placed in this stock. If no such stock exists,
        nothing will be done.

        :param item: Item that needs to be placed in the stock.
        :return: True if item was placed, False if not.

        PRE: Item is a product.
        POST: Item is placed in the right stock (according to its type), if this stock exists.
        """
        for list in self.stocks:
            if item.get_name() == list[0].get_name():
                list[len(list)] = item
                return True
        return False

    def is_empty(self, product_type):
        """ Determines if a certain stock is empty.

        :param product_type: stock that needs to be checked.
        :return: True if stock of product_type is empty, False if not.

        PRE: product_type is a string with the name of a product.
        POST: Stock is not affected. Returns True if stock is empty, False if not.
        """
        for list in self.stocks:
            if product_type == list[0].get_name():
                return not len(list) > 1
        return True

    def get_size(self, product_type):
        """ Determines the amount of products in a stock.

        :param product_type: stock that needs to be counted.
        :return: amount of products of type product_type in stock.

        PRE: product_type is a string with the name of a product.
        POST: Stock is not affected. Returns the amount of products of type product_type in stock.
        """
        for list in self.stocks:
            if product_type == list[0].get_name():
                return len(list)-1
        return 0

    def clean_stock(self, date):
        """ Cleans out expired products from the stock.

        Checks all stock-lists and deletes expired products from them. Returns a list of
        all the deleted products.

        :param date: current date
        :return: Deleted, expired items

        PRE: Date is used to check which expiration dates have already passed.
        POST: Stock does not contain any expired products anymore.
        """
        deleted = []
        self._sort()
        for list in self.stocks:
            to_delete = 0
            for i in range(1, len(list)):
                if list[i].get_expiration_date() < date:
                    to_delete += 1
                else:
                    break
            for j in range(to_delete):
                deleted.append(list[1])
                del list[1]
        return deleted

    def pop_item(self, product_type, date):
        """ Removes an item from the stock.

        Removes the product (of type 'product_type') with the most urgent expiration date from te corresponding
        stock-list. Products with expiration dates that have already passed will be ignored.

        :param product_type: Type of product that is needed.
        :param date: Date used as reference to check which expiration dates have already passed.
        :return: product if found, None if not.

        PRE: 'product_type' is a string corresponding to the item-type of a list in the stock.
        POST: If 'product_type corresponds to a type of the lists in the stock and this particular list contains an
        item with an expiration date "higher or equal to" the given date, then the item with the most urgent expiration
        date is removed from that list and returned.
        """
        for list in self.stocks:
            if product_type == list[0].get_name():
                return self._remove_by_date(list, date)
        return None

    def _sort(self):
        """ Sorts every stock-list by searchkey (expiration date).

        PRE: None.
        POST: Stocks are sorted.
        """
        for list in self.stocks:
            for sortFrom in range(1,len(list)):
                smallest = list[sortFrom]
                position = sortFrom
                for i in range(sortFrom, len(list)):
                    if list[i].get_searchkey() < smallest.get_searchkey():
                        smallest = list[i]
                        position = i
                sortFromItem = list[sortFrom]
                del list[position]
                list[position] = sortFromItem
                del list[sortFrom]
                list[sortFrom] = smallest

    def _remove_by_date(self, list, date):
        """ Removes the item with most urgent expiration date from the given stock-list.

        :param list: Stock-list from which an item is needed.
        :param date: Date used as reference to check which expiration dates have already passed.
        :return: product if found, None if not.

        PRE: 'date' is the date that is used as reference to check which expiration dates have already passed.
        POST: The item with most urgent expiration date is removed from the stock-list and this item with an expiration
        date "higher or equal" to 'date' is returned.
        """
        self._sort()
        for i in range(1, len(list)):
            if list[i].get_expiration_date() >= date:
                item_to_remove = list[i]
                del list[i]
                return item_to_remove
        return None

    def get_product_list(self):
        """ Makes a list of every product-type for which a separate stock-list exists.

        :return: list of names of the product-types in stock

        PRE: None.
        POST: A list with each different product-type is returned.
        """
        products = []
        for list in self.stocks:
            products.append(list[0].get_name())
        return products
