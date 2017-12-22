# import dll
from . import AdtDoublyLinkedList

LI0NEAR_PROBING = 0
QUADRATIC_PROBING = 1
SEPERATE_CHAINING = 2


class _DataNode:
    def __init__(self, search_key, data):
        self.search_key = search_key
        self.data = data

    def __del__(self):
        self.search_key = None
        self.data = None


class AdtHashMap:
    def __init__(self, length, collision_type):
        self.lijst = None
        # If the params are valid, create the main variables
        if self.create_hashmap(length, collision_type):
            self.length = length
            self.collision_type = collision_type

    def create_hashmap(self, length, collision_type):
        """
        Create a new hashmap.
        :param length: The length of the table.
        :param collision_type: The way to solve a collision.
        :return: True if the creation was succesfull, false otherwise.
        """
        # Input validation
        if 0 > collision_type > 2:
            print("Invalid collision_type!!")
            return False

        if length <= 0:
            print("Invalid length!")
            return False

        # Creating map
        self.lijst = []
        for i in range(length):
            self.lijst.append("")
        # If linked lists are used, fill every position with an empty link
        if collision_type == 2:
            for i in range(length):
                new_link = AdtDoublyLinkedList()
                self.lijst[i] = new_link
        return True

    def is_empty(self):
        """
        Checks if the list is empty.
        :return: True if list is empty, false otherwise
        """
        for item in self.lijst:
            if self.collision_type == 2:
                if not item.is_empty():
                    return False
            elif item != "":
                return False
        return True

    def table_insert(self, search_key, data):
        """
        Inserts a new element in the table.
        :param search_key: The new item to insert
        :param data: The data that needs to be stored
        :return: True if the insertion succeeded, false otherwise.
        """
        # Calculate adres and make datanode
        adres = self.calculate_address(search_key)
        new_node = _DataNode(search_key, data)
        # Check if a collision occurs
        if self.lijst[adres] != "":
            return self.solve_collision(adres, new_node, False)
        else:
            if self.collision_type == 2:
                self.lijst[adres].insertBeginning(new_node)
            else:
                self.lijst[adres] = new_node
            return True

    def calculate_address(self, search_key):
        """
        Calculates the adres with the hashfunction.
        :param search_key: The key to be used in the function
        :return: The adres calculated by the hash function.
        """
        adres = 0
        if isinstance(search_key, str):
            adres = len(search_key) % self.length
        elif isinstance(search_key, int):
            adres = search_key % self.length
        return adres

    def table_retrieve(self, search_key):
        """
        Returns an item from the hashmap.
        :param search_key: The item to search for and return.
        :return: item: The item that was found with the searchkey.
        :return: node: The node linked with the search_key or None if nothing was found
        """
        if self.is_empty():
            return False
        adres = self.calculate_address(search_key)
        if self.collision_type == 2:
            return self.solve_collision(adres, search_key, True)
        position = self.solve_collision(adres, search_key, True)
        node = self.lijst[position]
        return node

    def table_delete(self, search_key):
        """
        Deletes item from hashmap.
        :param search_key: Key from the node that needs to be deleted.
        :return: True if the deletion succeeded, false otherwise.
        """
        if self.is_empty():
            return False
        adres = self.calculate_address(search_key)
        if self.collision_type == 2:
            deleted = self.seperate_chaining(adres, search_key, True, True)
            if deleted:
                return deleted
            else:
                return True
        else:
            position = self.solve_collision(adres, search_key, True)
            if not position:
                return position
            else:
                self.lijst[position] = ""
                return True

    def solve_collision(self, adres, data, search):
        """
        Solves a collision by chosing from one of the methods.
        :param adres: Adres that caused collision
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :return: success, adres: Indicates wether the collision was solved. True if it was,
        false if it couldn't solve the collision.
        """
        if self.collision_type == 0:
            return self.linear_probing(adres, data, search)
        elif self.collision_type == 1:
            return self.quadratic_probing(adres, data, search)
        elif self.collision_type == 2:
            return self.seperate_chaining(adres, data, search, False)

    def linear_probing(self, adres, data, search):
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
            # Search through the list for the searchkey
            if search:
                if self.lijst[current_adres] != "":
                    if self.lijst[current_adres].search_key == data:
                        return current_adres
            # Insert element
            else:
                if self.lijst[current_adres] == "":
                    self.lijst[current_adres] = data
                    return True

            current_adres += 1
            count += 1

            if count == self.length:
                return False

            # Make sure to keep looping over the list
            if current_adres == self.length:
                current_adres = 0

    def quadratic_probing(self, adres, data, search):
        """
        Solve a collision with quadratic probing.
        :param adres: Adres that caused collision.
        :param data: The item to be inserted.
        :param search: Indicates if the algorithm has to search or not.
        :return: Indicates wether the collision was solved. True if it was,
        false if it couldn't solve the collision.
        """
        current_adres = adres
        # We put i on 2 because 1**2 is already visited by current_adres
        i = 1
        # Starts on 1 because we already visited the initial adres
        count = 1
        while True:
            # Search through the list for the searchkey
            if search:
                if self.lijst[current_adres] != "":
                    if self.lijst[current_adres].search_key == data:
                        return current_adres
            else:
                if self.lijst[current_adres] == "":
                    self.lijst[current_adres] = data
                    return True

            current_adres = (adres + i**2) % self.length
            i += 1
            count += 1

            # Check if the whole list was checked
            if count == self.length:
                return False

            # if current_adres >= self.length:
            #     current_adres = 0

    def seperate_chaining(self, adres, data, search, delete):
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
            length = table.get_length()
            current_link = table.head
            counter = 0
            while counter != length:
                if current_link.item.search_key == data:
                    if delete:
                        table.delete(counter)
                    else:
                        return current_link.item
                else:
                    current_link = current_link.next
                    counter += 1
            return False
        else:
            self.lijst[adres].insert_beginning(data)
            return True
