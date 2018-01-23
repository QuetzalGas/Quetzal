from .datastructures import *
from .product import *
from .date import *

class Stock:
    def __init__(self, products, type_):
        """ Creates empty lists for the given products.

        :param products list of the different products that need a stock

        PRE: Type is a circular linked list (CLL) or a doubly linked list (DLL). Type decides the kind of
        implementation of the stocks. Products are passed as a list of unique strings.
        POST: The stock contains as many lists as there are different products.
        """
        self.stocks = []
        for product in products:
            new_stock = type_()
            new_stock[0] = Product(product, 0, 0, Date(0,0,0))
            self.stocks.append(new_stock)

    def add_item(self, item):
        """ Adds an item to the stock.

        If there is a stock that the item belongs in, the item will be placed in this stock. If no such stock exists,
        nothing will be done.

        :param item: Item that needs to be placed in the stock.
        :raise KeyError if stock for item doesn't exist
        :return: True if item was placed, False if not.

        PRE: Item is a product.
        POST: Item is placed in the right stock (according to its type), if this stock exists.
        """
        for stock_list in self.stocks:
            if item.get_name() == stock_list[0].get_name():
                stock_list[len(stock_list)] = item
                return True
        raise KeyError

    def is_empty(self, product_name):
        """ Determines if a certain stock is empty.

        :param product_name: stock that needs to be checked.
        :return: True if stock of product_name is empty, False if not.

        PRE: product_name is a string with the name of a product.
        POST: Stock is not affected. Returns True if stock is empty, False if not.
        """
        for stock_list in self.stocks:
            if product_name == stock_list[0].get_name():
                return not len(stock_list) > 1
        return True

    def get_size(self, product_name):
        """ Determines the amount of products in a stock.

        :param product_name: stock that needs to be counted.
        :return: amount of products of type product_name in stock.

        PRE: product_name is a string with the name of a product.
        POST: Stock is not affected. Returns the amount of products of type product_name in stock.
        """
        for stock_list in self.stocks:
            if product_name == stock_list[0].get_name():
                return len(stock_list)-1
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
        for stock_list in self.stocks:
            self._sort(stock_list)
            to_delete = 0
            for i in range(1, len(stock_list)):
                if stock_list[i].get_expiration_date() < date:
                    to_delete += 1
                else:
                    break
            for j in range(to_delete):
                deleted.append(stock_list[1])
                del stock_list[1]
        return deleted

    def pop_item(self, product_name, date):
        """ Removes an item from the stock.

        Removes the product (of type 'product_name') with the most urgent expiration date from te corresponding
        stock-list. Products with expiration dates that have already passed will be ignored.

        :param product_name: Type of product that is needed.
        :param date: Date used as reference to check which expiration dates have already passed.
        :return: product if found, None if not.

        PRE: 'product_name' is a string corresponding to the item-type of a list in the stock.
        POST: If 'product_name corresponds to a type of the lists in the stock and this particular list contains an
        item with an expiration date "higher or equal to" the given date, then the item with the most urgent expiration
        date is removed from that list and returned.
        """
        for stock_list in self.stocks:
            if product_name == stock_list[0].get_name():
                return self._remove_by_date(stock_list, date)
        return None

    def _sort(self, stock_list):
        """ Sorts the given stock-list by searchkey (expiration date).

        PRE: None.
        POST: Stock-list is sorted.
        """
        for sortFrom in range(1,len(stock_list)):
            smallest = stock_list[sortFrom]
            position = sortFrom
            for i in range(sortFrom, len(stock_list)):
                if stock_list[i].get_searchkey() < smallest.get_searchkey():
                    smallest = stock_list[i]
                    position = i
            sortFromItem = stock_list[sortFrom]
            del stock_list[position]
            stock_list[position] = sortFromItem
            del stock_list[sortFrom]
            stock_list[sortFrom] = smallest

        # sorted = False
        # if self.type == "cll":
        #     for area in range(1, stockList.get_length()):
        #         if not sorted:
        #             sorted = True
        #             for i in range(1, stockList.get_length() - area + 1):
        #                 (place_i, bool) = stockList.retrieve(i)
        #                 (place_after, bool) = stockList.retrieve(i + 1)
        #
        #                 if place_after.get_expiration_date() < place_i.get_expiration_date():
        #                     sorted = False
        #
        #                     stockList.insert(i, place_after)
        #                     stockList.delete(i + 2)

    def _remove_by_date(self, stock_list, date):
        """ Removes the item with most urgent expiration date from the given stock-list.

        :param stock_list: Stock-list from which an item is needed.
        :param date: Date used as reference to check which expiration dates have already passed.
        :return: product if found, None if not.

        PRE: 'date' is the date that is used as reference to check which expiration dates have already passed.
        POST: The item with most urgent expiration date is removed from the stock-list and this item with an expiration
        date "higher or equal" to 'date' is returned.
        """
        self._sort(stock_list)
        for i in range(1, len(stock_list)):
            if stock_list[i].get_expiration_date() >= date:
                item_to_remove = stock_list[i]
                del stock_list[i]
                return item_to_remove
        return None

    def get_product_list(self):
        """ Makes a list of every product-type for which a separate stock-list exists.

        :return: list of names of the product-types in stock

        PRE: None.
        POST: A list with the name of each different product-type is returned.
        """
        products = []
        for stock_list in self.stocks:
            products.append(stock_list[0].get_name())
        return products
