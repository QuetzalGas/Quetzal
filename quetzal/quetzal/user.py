from .datastructures import *


class UserContainer:
    """
    Contains all users (customers) and their orders. The initializing of a user starts here.
    When a user gives their firstname, lastname and email-address the ID is calculated, the email is used to
    check whether the user is new or not. A new customer will be added to the table. (stored in BS, 23, 234 or RB tree)
    """

    def __init__(self, table):
        """
        :param table: The table of type: AdtBinarySearchTree, AdtTwoThreeTree, AdtTwoThreeFourTree, AdtRedBlacktree
                      or Hashmap.
        :raise: If the table is of incorrect type, an exception is raised.
        """
        self.idcounter = 0
        self.table = table
        if not (isinstance(table, AdtBinarySearchTree) or isinstance(table, AdtTwoThreeTree) or
                isinstance(table, AdtHashMap) or isinstance(table, AdtTwoThreeFourTree) or
                isinstance(table, AdtRedBlackTree)):
            raise TypeError("Unvalid table type for the UserContainer.")

    def add_if_unknown_user(self, firstname, lastname, email):
        """ Checks whether a user with the given 'email' is already present in the table, if not a new User is added
        to the table with the given 'firstname', 'lastname' and 'email'.

        :param :   'firstname', 'lastname' and 'email' are strings.
        :return:   True if a new user was added, False otherwise.
        """
        if email in self.table:
            return False
        else:
            new_user = User(self.calculate_id(), firstname, lastname, email)
            self.table[email] = new_user
            return True

    def retrieve_user(self, email):
        """ Searches for a user by the given 'email'.

        :param :   'email' is the email adress of the user that should be found.
        :return:   If there was a user with email adress 'email' in the table, True and the User is returned.
                   If not, False and None is returned.
        """
        if not email in self.table:
            return False, None
        return True, self.table[email]

    def is_empty(self):
        """ Checks whether the table is empty or not.

        :return:   True if the table is empty, False otherwise.
        """
        return self.table.is_empty()

    def calculate_id(self):
        id_ = self.idcounter
        self.idcounter += 1
        return id_

    def get_graph(self):
        return repr(self.table)

class User:
    """
    A customer of the chocolade bar.
    """

    def __init__(self, id_, firstname, lastname, email):
        """ Initializes a new customer with their name, email and unique id.

        :param :   'id' is the unique id of the user. 'firstname', 'lastname' and 'email' are data of the user.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id_

    def get_id(self):
        """
        :return :   Returns the ID of the user.
        """
        return self.id

    def get_firstname(self):
        """
        :return :   Returns the first name of the user.
        """
        return self.firstname

    def get_lastname(self):
        """
        :return :   Returns the last name of the user.
        """
        return self.lastname

    def get_email(self):
        """
        :return :   Returns the email adress of the user.
        """
        return self.email

    def __str__(self):
        return self.firstname + " " +self.lastname