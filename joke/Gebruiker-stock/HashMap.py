from Double_Linked_Lists import Double_Linked_List
from DataNode import DataNode

LI0NEAR_PROBING = 0
QUADRATIC_PROBING = 1
SEPERATE_CHAINING = 2

class HashMap:
    def __init__(self, length, collisiontype):
        self.lijst = None
        #If the params are valid, create the main variables
        if self.createHashMap(length, collisiontype):
            self.length = length
            self.collisionType = collisiontype

    def createHashMap(self, length, collisiontype):
        """
        Create a new hashmap.
        :param length: The length of the table.
        :param collisiontype: The way to solve a collision.
        :return: True if the creation was succesfull, false otherwise.
        """
        #Input validation
        if 0 > collisiontype > 2:
            print("Invalid collisiontype!!")
            return False

        if length <= 0:
            print("Invalid length!")
            return False

        #Creating map
        self.lijst = []
        for i in range(length):
            self.lijst.append("")
        #If linked lists are used, fill every position with an empty link
        if collisiontype == 2:
            for i in range(length):
                new_link = Double_Linked_List()
                self.lijst[i] = new_link
        return True

    def isEmpty(self):
        """
        Checks if the list is empty.
        :return: True if list is empty, false otherwise
        """
        for item in self.lijst:
            if self.collisionType == 2:
                if not item.isEmpty():
                    return False
            elif item != "":
                return False
        return True

    def tableInsert(self, searchKey, data):
        """
        Inserts a new element in the table.
        :param searchKey: The new item to insert
        :param data: The data that needs to be stored
        :return: True if the insertion succeeded, false otherwise.
        """
        #Calculate adres and make datanode
        adres = self.calculateAdres(searchKey)
        new_node = DataNode(searchKey, data)
        #Check if a collision occurs
        if self.lijst[adres] != "":
            return self.solveCollision(adres, new_node, False)
        else:
            if self.collisionType == 2:
                self.lijst[adres].insertBeginning(new_node)
            else:
                self.lijst[adres] = new_node
            return True

    def calculateAdres(self, searchKey):
        """
        Calculates the adres with the hashfunction.
        :param searchKey: The key to be used in the function
        :return: The adres calculated by the hash function.
        """
        adres = 0
        if type(searchKey) is str:
            adres = len(searchKey) % self.length
        elif type(searchKey) is int:
            adres = searchKey % self.length
        return adres

    def tableRetrieve(self, searchKey):
        """
        Returns an item from the hashmap.
        :param searchKey: The item to search for and return.
        :return: item: The item that was found with the searchkey.
        :return: node: The node linked with the searchKey or None if nothing was found
        """
        if self.isEmpty():
            return False
        adres = self.calculateAdres(searchKey)
        if self.collisionType == 2:
            return self.solveCollision(adres, searchKey, True)
        position = self.solveCollision(adres, searchKey, True)
        node = self.lijst[position]
        return node

    def tableDelete(self, searchKey):
        """
        Deletes item from hashmap.
        :param searchKey: Key from the node that needs to be deleted.
        :return: True if the deletion succeeded, false otherwise.
        """
        if self.isEmpty():
            return False
        adres = self.calculateAdres(searchKey)
        if self.collisionType == 2:
            deleted = self.seperateChaining(adres, searchKey, True, True)
            if deleted:
                return deleted
            else:
                return True
        else:
            position = self.solveCollision(adres, searchKey, True)
            if position == False:
                return position
            else:
                self.lijst[position] = ""
                return True

    def solveCollision(self, adres, data, search):
        """
        Solves a collision by chosing from one of the methods.
        :param adres: Adres that caused collision
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :return: success, adres: Indicates wether the collision was solved. True if it was,
        false if it couldn't solve the collision.
        """
        if self.collisionType == 0:
            return self.linearProbing(adres, data, search)
        elif self.collisionType == 1:
            return self.quadraticProbing(adres, data, search)
        elif self.collisionType == 2:
            return self.seperateChaining(adres, data, search, False)

    def linearProbing(self, adres, data, search):
        """
        Solve a collision with linear probing.
        :param adres: Adres that caused collision.
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :return: Indicates wether the collision was solved. True if it was,
        false if it couldn't solve the collision.
        """
        current_adres = adres
        count = 0
        while True:
            #Search through the list for the searchkey
            if search:
                if self.lijst[current_adres] != "":
                    if self.lijst[current_adres].searchKey == data:
                        return current_adres
            #Insert element
            else:
                if self.lijst[current_adres] == "":
                    self.lijst[current_adres] = data
                    return True

            current_adres += 1
            count += 1

            if count == self.length:
                return False

            #Make sure to keep looping over the list
            if current_adres == self.length:
                current_adres = 0

    def quadraticProbing(self, adres, data, search):
        """
        Solve a collision with quadratic probing.
        :param adres: Adres that caused collision.
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :return: Indicates wether the collision was solved. True if it was,
        false if it couldn't solve the collision.
        """
        current_adres = adres
        #We put i on 2 because 1**2 is already visited by current_adres
        i = 1
        #Starts on 1 because we already visited the initial adres
        count = 1
        while True:
            #Search through the list for the searchkey
            if search:
                if self.lijst[current_adres] != "":
                    if self.lijst[current_adres].searchKey == data:
                        return current_adres
            else:
                if self.lijst[current_adres] == "":
                    self.lijst[current_adres] = data
                    return True

            current_adres = (adres + i**2)%self.length
            i += 1
            count += 1

            #Check if the whole list was checked
            if count == self.length:
                return False

            # if current_adres >= self.length:
            #     current_adres = 0

    def seperateChaining(self, adres, data, search, delete):
        """
        Solve a collision with seperate chaining.
        :param adres: Adres that caused collision.
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :param delete: Indicates if the algorithm has to delete or not.
        :return: Indicates wether the collision was solved or the item found. True if it was,
        false if it couldn't solve the collision.
        """
        if search:
            table = self.lijst[adres]
            length = table.getLength()
            current_link = table.head
            counter = 0
            while counter != length:
                if current_link.item.searchKey == data:
                    if delete:
                        table.delete(counter)
                    else:
                        return current_link.item
                else:
                    current_link = current_link.next
                    counter += 1
            return False
        else:
            self.lijst[adres].insertBeginning(data)
            return True


