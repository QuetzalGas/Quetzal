class ChocolateMilk:
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.contains = []
        self.workload = 5

    def getId(self):
        """

        :return:
        """
        return self.id

    def getIngredients(self):
        """

        :return:
        """
        return self.contains

    def getWorkLoad(self):
        """

        :return:
        """
        return self.workload

    def getTotalPrice(self):
        """

        :return:
        """
        return self.price

    def addProduct(self, product):
        """

        :param product:
        :return:
        """
        self.contains.append(product)
        self.workload += 1
        self.price += product.getPrice()

