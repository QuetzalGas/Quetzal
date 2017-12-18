from Double_Linked_Lists import Double_Linked_List

class ChocolateMilk:
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.contains = Double_Linked_List()
        self.workload = 5

    def getId(self):
        """
        Returns the id of the chocolatemilk.
        :return: The id.
        """
        return self.id

    def getIngredients(self):
        """
        Returns the ingredients in the chocolatemilk.
        :return: A list with all the
        """
        return self.contains

    def getWorkLoad(self):
        """
        Returns the workload the chocolatemilk creates.
        :return:
        """
        return self.workload

    def getTotalPrice(self):
        """
        Returns the total price of the chocolatemilk.
        :return:
        """
        return self.price

    def addProduct(self, product):
        """
        Add a product to the chocolatemilk.
        :param product: The product to be added
        :return:
        """
        self.contains.insertBeginning(product)
        self.workload += 1
        self.price += product.getPrice()

