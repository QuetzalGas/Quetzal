from datastructures import *
from order import Order

class UserContainer:
    """
    Contains all users (customers) and their orders. The initializing of a user starts here.
    When a user gives their firstname, lastname and email-address the ID is calculated, the email is used to
    check whether the user is new or not. If it's a new customer, then this customer will be added to the
    users. (stored in BS, 23, 234 or RB tree)
    PRE :   'type' decided whether the users will be stored in a 23, 234 or RB-tree or hashmap (type == 23 or 234 or rb or h)
    POST:   Depending op 'type', the UserContainer now contains a table which is a 23, 234, rb or BS tree or a hashmap.
    """
    def __init__(self, type):
        self.idcounter = 0
        if type == 'bs' or type == 'BS':
            self.type = 'bs'
            self.table = AdtBinarySearchTree()
        elif type == '23':
            self.type = '23'
            self.table = AdtTwoThreeTree()
        elif type == '234':
            self.type = '234'
            self.table = AdtTwoThreeFourTree()
        elif type == 'rb' or type == 'RB':
            self.type = 'rb'
            self.table = AdtRedBlackTree()
        elif type == 'h' or type == 'H':
            self.type = 'h'
            self.table = AdtHashMap(254, 2)  # 254 is the max length of a valid email-address
        else:
            print("Unvalid type.")

    def check_user(self, order, firstname, lastname, email):
        """
        Checks whether a user with the given 'email' is already present in the table, if not a new User is added to the table
        with the given 'firstname', 'lastname', 'email' and 'order'.
        PRE :   'order' is of type Order; 'firstname', 'lastname' and 'email' are strings
        POST:   If there wasn't yet a user with the given 'email', a new User is added to the table. The 'order' is added
                to the order-list of the user (new user or not).
        """
        if self.type == 'bs':
            result = self.table.searchTreeRetrieve(email)
            resultRetrieve = result[0]
            if resultRetrieve is not False:
                retrievedItem = result[1].item
        elif self.type == '23':
            result = self.table.retrieveItem(email)
            resultRetrieve = result[1]
            retrievedItem = result[0]
        elif self.type == '234':
            result = self.table.tableRetrieve(email)
            resultRetrieve = result[1]
            if result[0] is not None:
                retrievedItem = result[0].item
        # elif self.type == 'rb':
        #     resultRetrieve =
        else:   #hashmap
            resultRetrieve = self.table.tableRetrieve(email)
            retrievedItem = resultRetrieve  # Hashmap return False or Node, zo not a tuple

        if(resultRetrieve is not False):
            if self.type == 'h':
                retrievedItem = retrievedItem.data
            retrievedItem.add_order(order)
        else:
            user = User(self.calculate_id(), firstname, lastname, email)
            user.add_order(order)
            self.add_new_user(user)

    def add_new_user(self, user):
        """
        Adds a new user to the container. This method is not supposed to be used by an outsider, it's used inside the
        check_user method.
        PRE :   'user' is of type User.
        POST:   'user' is added to the table.
        """
        if self.type == 'bs':
            self.table.insert(user.email, user)
        elif self.type == '23':
            self.table.insertItem(user.email, user)
        elif self.type == '234':
            self.table.tableInsert(user.email, user)
        elif self.type == 'rb':
            self.table.insert(user.email, user)
        elif self.type == 'h':
            self.table.tableInsert(user.email, user)

    def retrieve_user(self, email):
        """
        Searches for a user by the given 'email'.
        PRE :   'email' is the email adress of the user that should be found.
        POST:   If there was a user with email adress 'email' in the table, then this User and a boolean True is returned.
                If there wasn't a user with 'email' as email adress, None and False is returned.
        """
        if self.type == 'bs':
            user = self.table.searchTreeRetrieve(email)[1]
            if user is not None:
                user = user.item
        elif self.type == '23':
            user = self.table.retrieveItem(email)[0]
        elif self.type == '234':
            user = self.table.tableRetrieve(email)[0]
            if user is not None:
                user = user.item
        # elif self.type == 'rb':
        #     resultRetrieve =
        else:  # hashmap
            user = self.table.tableRetrieve(email)
        if (user is False or user is None):
            return False, None
        else:
            if self.type == "h":
                user = user.data
            return True, user

    def is_empty(self):
        """
        Checks whether the table is empty or not.
        PRE :   None
        POST:   True is returned if the table is empty.
        """
        if self.type == 'bs' or self.type == '23' or self.type == '234':
            return self.table.tableIsEmpty()
        if self.type == 'h':
            return self.table.isEmpty()

    def calculate_id(self):
        id = self.idcounter
        self.idcounter += 1
        return id

class User:
    """
    A customer of the chocolade bar.
    """
    def __init__(self, id,  firstname, lastname, email):
        """
        Initializes a new customer with their name, email and unique id.
        PRE :   'id' is the unique id of the user. 'firstname', 'lastname' and 'email' are data of the user.
        POST:   The user now contains a unique id, user data and a list of orders.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id
        self.orders = list()

    def add_order(self, order):
        """
        Adds the order to the list of orders of the specific user.
        PRE:    'order' is of type Order.
        POSR:   The order-list is returned.
        """
        if isinstance(order, Order):
            return False
        self.orders.append(order)
        return True

    def calculate_id(self):
        """
        Calculates the user's ID.
        PRE :   None
        POST:   The freshly calculates ID is returned.
        """
        for char in self.email:
            self.id += ord(char)
            self.id *= 10

    def get_orders(self):
        """
        PRE :   None
        POST:   Returns a list of all orders of the user.
        """
        return self.orders

    def get_id(self):
        """
        PRE :   None
        POST:   Returns the ID of the user.
        """
        return self.id

    def get_firstname(self):
        """
        PRE :   None
        POST:   Returns the first name of the user.
        """
        return self.firstname

    def get_lastname(self):
        """
        PRE :   None
        POST:   Returns the last name of the user.
        """
        return self.lastname

    def get_email(self):
        """
        PRE :   None
        POST:   Returns the email adress of the user.
        """
        return self.email