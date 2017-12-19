class Product:
    def __init__(self, name, price, workload, expiration_date):
        self.name = name
        self.price = price
        self.workload = workload
        self.expiration_date = expiration_date

    def get_price(self):
        """
        Returns the price of the product.
        PRE: None.
        POST: Return value is the price of the product.
        :return: price
        """
        return self.price

    def get_expiration_date(self):
        """
        Returns the expiration date of the product.
        PRE: None.
        POST: return value is the expiration date of the product.
        :return: expirationdate
        """
        return self.expiration_date

    def get_name(self):
        """
        Returns the name of the product.
        PRE: None.
        POST: Return value is the name of the product.
        :return: name
        """
        return self.name

    def get_workload(self):
        """
        Returns the workload of the product.
        PRE: None.
        POST: Return value is the workload of the product.
        :return: workload
        """
        return self.workload

    def get_searchkey(self):
        """
        Returns the search key of the product, which is the expiration date.
        PRE: None.
        POST: Return value is the search key of the product.
        :return: expirationdate
        """
        return self.expiration_date

class Chilipepper(Product):
    def __init__(self, expiration_date):
        super().__init__("chilipeper", 0.25, 1, expiration_date)

class Honey(Product):
    def __init__(self, expiration_date):
        super().__init__("honing", 0.5, 1, expiration_date)

class Marshmallow(Product):
    def __init__(self, expiration_date):
        super().__init__("marshmallow", 0.75, 1, expiration_date)

class Chocolateshot(Product):
    def __init__(self, expiration_date, taste):
        allowed_tastes = ["melk", "zwart", "wit", "bruin"]
        if taste in allowed_tastes:
            super().__init__(taste, 1, 1, expiration_date)
        else:
            raise ValueError("")
