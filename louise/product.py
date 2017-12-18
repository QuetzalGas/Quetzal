class Product:
    def __init__(self, name, price, workload, expirationdate):
        self.name = name
        self.price = price
        self.workload = workload
        self.expirationdate = expirationdate

    def getPrice(self):
        """
        Returns the price of the product.
        PRE: None.
        POST: Return value is the price of the product.
        :return: price
        """
        return self.price

    def getExpirationdate(self):
        """
        Returns the expiration date of the product.
        PRE: None.
        POST: return value is the expiration date of the product.
        :return: expirationdate
        """
        return self.expirationdate

    def getName(self):
        """
        Returns the name of the product.
        PRE: None.
        POST: Return value is the name of the product.
        :return: name
        """
        return self.name

    def getWorkload(self):
        """
        Returns the workload of the product.
        PRE: None.
        POST: Return value is the workload of the product.
        :return: workload
        """
        return self.workload

    def getSearchKey(self):
        """
        Returns the search key of the product, which is the expiration date.
        PRE: None.
        POST: Return value is the search key of the product.
        :return: expirationdate
        """
        return self.expirationdate

class Chilipeper(Product):
    def __init__(self, expirationdate):
        super().__init__("chilipeper", 0.25, 1, expirationdate)

class Honing(Product):
    def __init__(self, expirationdate):
        super().__init__("honing", 0.5, 1, expirationdate)

class Marshmallow(Product):
    def __init__(self, expirationdate):
        super().__init__("marshmallow", 0.75, 1, expirationdate)

class Chocoladeshot(Product):
    def __init__(self, expirationdate, taste):
        allowed_tastes = ["melk", "zwart", "wit"]
        if taste in allowed_tastes:
            super().__init__(taste, 1, 1, expirationdate)

