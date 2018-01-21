from .datastructures import *


class UserContainer:
    """
    Contains all users (customers) and their orders. The initializing of a user starts here.
    When a user gives their firstname, lastname and email-address the ID is calculated, the email is used to
    check whether the user is new or not. If it's a new customer, then this customer will be added to the
    users. (stored in BS, 23, 234 or RB tree)
    PRE :   'type' decides whether the users will be stored in a BS, 23, 234 or RB-tree or Hashmap
    POST:   Depending on 'type', the UserContainer now contains a table that is a BS, 23, 234 or RB-tree or a Hashmap.
    """

    def __init__(self, type):
        self.idcounter = 0

        # # How it should be:
        # self.table = type

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
            # 254 is the max length of a valid email-address
            self.table = AdtHashMap(254, 2)
        else:
            raise ValueError("Unvalid type.")

    def add_if_unknown_user(self, firstname, lastname, email):
        """ Checks whether a user with the given 'email' is already present in the table, if not a new User is added
        to the table with the given 'firstname', 'lastname', 'email' and 'order'.

        :param :   'order' is of type Order; 'firstname', 'lastname' and 'email' are strings.
        :return:   True if a new user was added, False otherwise.
        """
        # # How it should be:
        # if self.table.__contains__(email):
        #     return False
        # else:
        #     new_user = User(self.calculate_id(), firstname, lastname, email)
        #     self.table.__setitem__(email, new_user)
        #     return True

        if self.type == 'bs':
            result = self.table.__getitem__(email)
            resultRetrieve = result[0]
            if resultRetrieve is not False:
                retrievedItem = result[1].item
        elif self.type == '23':
            result = self.table.__getitem__(email)
            resultRetrieve = result[1]
            retrievedItem = result[0]
        elif self.type == '234':
            result = self.table.table_retrieve(email)
            resultRetrieve = result[1]
            if result[0] is not None:
                retrievedItem = result[0].item
        # elif self.type == 'rb':
        #     resultRetrieve =
        else:  # hashmap
            resultRetrieve = self.table.table_retrieve(email)
            retrievedItem = resultRetrieve  # Hashmap return False or Node, zo not a tuple

        if(resultRetrieve is not False):
            return False
        else:
            user = User(self.calculate_id(), firstname, lastname, email)
            self._add_new_user(user)
            return True

    def _add_new_user(self, user):
        """ Adds a new user to the container. This method is not supposed to be used by an outsider, it's used
        inside the check_user method.

        :param user :   'user' is of type User. This will be added to the table.
        """
        ## How it should be:
        # This method wouldn't be needed anymore.

        if self.type == 'bs':
            self.table.__setitem__(user.email, user)
        elif self.type == '23':
            self.table.__setitem__(user.email, user)
        elif self.type == '234':
            self.table.table_insert(user.email, user)
        elif self.type == 'rb':
            self.table.insert(user.email, user)
        elif self.type == 'h':
            self.table.__setitem__(user.email, user)

    def retrieve_user(self, email):
        """ Searches for a user by the given 'email'.

        :param :   'email' is the email adress of the user that should be found.
        :return:   If there was a user with email adress 'email' in the table, True and the User is returned.
                   If not, False and None is returned.
        """
        # How it should be:
        # (boolean, user) = self.table.__getitem__(email)
        # if boolean:
        #     return True, user
        # else:
        #     return False, None
        # ####

        if self.type == 'bs':
            user = self.table.__getitem__(email)[1]
            if user is not None:
                user = user.item
        elif self.type == '23':
            user = self.table.__getitem__(email)[1]
        elif self.type == '234':
            user = self.table.table_retrieve(email)[0]
            if user is not None:
                user = user.item
        # elif self.type == 'rb':
        #     resultRetrieve =
        else:  # hashmap
            user = self.table.__getitem__(email)
        if (user is False or user is None):
            return False, None
        else:
            if self.type == "h":
                user = user.data
            return True, user

    def is_empty(self):
        """ Checks whether the table is empty or not.

        :return:   True if the table is empty, False otherwise.
        """
        ## How it should be:
        # return self.table.is_empty()

        if self.type == 'bs' or self.type == '23':
            return self.table.is_empty()
        if self.type == '234':
            return self.table.table_is_empty()
        if self.type == 'h':
            return self.is_empty()

    def calculate_id(self):
        id_ = self.idcounter
        self.idcounter += 1
        return id_


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
