import uuid     # for unique IDs
from HashMap import HashMap
from binaireZoekboom import TreeItem, BinarySearchTree
from twoThreeTree import TwoThreeTree
from rb_tree import Node, RbTree
from TwoThreeFourTree import TwoThreeFourTree

class Order:
    def __init__(self):
        self.something = 0

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
        if type == 'bs' or type == 'BS':
            self.type = 'bs'
            self.table = BinarySearchTree()
        elif type == '23':
            self.type = '23'
            self.table = TwoThreeTree()
        elif type == '234':
            self.type = '234'
            self.table = TwoThreeFourTree()
        elif type == 'rb' or type == 'RB':
            self.type = 'rb'
            self.table = RbTree()
        elif type == 'h' or type == 'H':
            self.type = 'h'
            self.table = HashMap(254, 2)  # 254 is the max length of a valid email-address
        else:
            print("Unvalid type.")

    def checkUser(self, order, firstname, lastname, email):
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
            retrievedItem.addOrder(order)
        else:
            user = User(firstname, lastname, email)
            user.addOrder(order)
            self.addNewUser(user)

    def addNewUser(self, user):
        """
        Adds a new user to the container. This method is not supposed to be used by an outsider, it's used inside the
        checkUser method.
        PRE :   'user' is of type User.
        POST:   'user' is added to the table.
        """
        if self.type == 'bs':
            self.table.searchTreeInsert(TreeItem(user.email, user))
        elif self.type == '23':
            self.table.insert(TreeItem(user.email, user))
        elif self.type == '234':
            self.table.tableInsert(TreeItem(user.email, user))
        elif self.type == 'rb' or type == 'RB':
            self.table.insert(user.email, user)
        elif self.type == 'h':
            self.table.tableInsert(user.email, user)

    def retrieveUser(self, email):
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

    def isEmpty(self):
        """
        Checks whether the table is empty or not.
        PRE :   /
        POST:   True is returned if the table is empty.
        """
        if self.type == 'bs' or self.type == '23' or self.type == '234':
            return self.table.tableIsEmpty()
        if self.type == 'h':
            return self.table.isEmpty()

class User:
    """
    A customer of the chocolade bar.
    """
    def __init__(self, firstname, lastname, email):
        """
        Initializes a new customer with their name, email and unique id.
        PRE :   'id' is the unique id of the user. 'firstname', 'lastname' and 'email' are data of the user.
        POST:   The user now contains a unique id, user data and a list of orders.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = 0
        self.orders = list()

        for character in email:
            self.id += ord(character)

    def addOrder(self, order):
        """
        Adds the order to the list of orders of the specific user.
        PRE:    'order' is of type Order.
        POSR:   The order-list is returned.
        """
        if isinstance(order, Order):
            return False
        self.orders.append(order)
        return True

    def calculateID(self):
        """
        Calculates the user's ID.
        PRE :   /
        POST:   The freshly calculates ID is returned.
        """
        for char in self.email:
            self.id += ord(char)
            self.id *= 10

    def getOrders(self):
        """
        PRE :   /
        POST:   Returns a list of all orders of the user.
        """
        return self.orders

    def getID(self):
        """
        PRE :   /
        POST:   Returns the ID of the user.
        """
        return self.id

    def getFirstname(self):
        """
        PRE :   /
        POST:   Returns the first name of the user.
        """
        return self.firstname

    def getLastname(self):
        """
        PRE :   /
        POST:   Returns the last name of the user.
        """
        return self.lastname

    def getEmail(self):
        """
        PRE :   /
        POST:   Returns the email adress of the user.
        """
        return self.email

def printListy(listy):
    if not listy.isEmpty():
        cur = listy.head
        print('\n')
        for i in range(0, listy.getLength()):
            print(cur.item.data.getFirstname(), ", ", end="")
            cur = cur.next

def printHashmap(hash):
    print("=======================")
    for i in hash.lijst:
        printListy(i)
    print('\n=======================')
