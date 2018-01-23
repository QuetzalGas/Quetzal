from .datastructures import *

class ChocolateMilk:
    def __init__(self, id_):
        """
        Initialises a new chocolatemilk.
        :param id: The id of the chocolatemilk.
        POST: A new chocolatemilk was created with a default price and workload.
        """
        self.id = id_
        self.price = 2
        self.contains = AdtDoublyLinkedList()
        self.workload = 5

    def get_id(self):
        """
        Returns the id of the chocolatemilk.
        :return: The id of the chocolatemilk.
        """
        return self.id

    def get_ingredients(self):
        """
        Returns the ingredients in the chocolatemilk.
        :return: A double linked list with all the ingredients.
        """
        return self.contains

    def get_workload(self):
        """
        Returns the workload the chocolatemilk creates.
        :return: The workload of the employee.
        """
        return self.workload

    def get_total_price(self):
        """
        Returns the total price of the chocolatemilk.
        :return: The total price of the chocolatemilk.
        """
        return self.price

    def add_product(self, product):
        """
        Add a product to the chocolatemilk.
        :param product: The product to be added.
        PRE: Procuct has of the Product class and can't be empty.
        """
        self.contains[0] = (product,)
        self.workload += 1
        self.price += product.get_price()
