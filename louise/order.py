class Order:
    def __init__(self, userID, time, itemID):
        """
        Initializes an order, which contains a user-id, a timestamp and an id of the chocolate milk.
        PRE: UserID is the id of the user that placed the order, time is the timestamp of the order and itemID is the id of the chocolate milk being ordered.
        POST: The order contains a userID, a timestamp and an itemID and has not been collected.
        :param userID: id of the user that placed the order
        :param time: timestamp of the order
        :param itemID: id of the chocolate milk being ordered
        """
        self.userID = userID
        self.time = time
        self.itemID = itemID
        self.collected = False

    def is_collected(self):
        """
        Checks if the order has already been collected.
        PRE: None.
        POST: Returns True if collected, False if not.
        :return: collected
        """
        return self.collected

    def set_collected(self):
        """
        Puts the status of the order to collected.
        PRE: None.
        POST: The order has been collected.
        """
        self.collected = True

    def getUserID(self):
        """
        Returns user-id.
        PRE: None.
        POST: User-id is returned.
        :return: user-id
        """
        return self.userID

    def getTime(self):
        """
        Returns timestamp
        PRE: None.
        POST: Timestamp is returned.
        :return: time
        """
        return self.time

    def getItemID(self):
        """
        Returns id of the chocolate milk.
        PRE: None.
        POST: Chocolatemilk-id is returned.
        :return: itemID
        """
        return self.itemID

    def getSearchKey(self):
        """
        Returns the search key of the order, which is the timestamp.
        PRE: None.
        POST: Search key is returned.
        :return: searchkey
        """
        return self.time



