# import dll
from . import AdtDoublyLinkedList

LINEAR_PROBING = 0
QUADRATIC_PROBING = 1
SEPARATE_CHAINING = 2


class _DataNode:
    def __init__(self, search_key, data):
        """ Creates new datanode.

        :param search_key: The searchkey of the node.
        :param data: The data of the node.
        """
        self.search_key = search_key
        self.data = data

    def __del__(self):
        self.search_key = None
        self.data = None


class AdtHashMap:
    def __init__(self, length=10, collision_type=2): #TODO default value list
        """ Initialises a new hashmap with a certain length and collision type.

        :param length: The length of the hashmap.
        :param collision_type: The way to solve a collision.
        """
        self.lijst = None
        # If the params are valid, create the main variables
        self._create_hashmap(length, collision_type)
        self.length = length
        self.collision_type = collision_type

    def __del__(self):
        """
        Deletes the hashmap.
        """
        self.lijst = None
        self.length = 0
        self.collision_type = None

    def _create_hashmap(self, length, collision_type):
        """ Create a new hashmap.

        :param length: The length of the table.
        :param collision_type: The way to solve a collision.
        """
        # Input validation
        if 0 > collision_type > 2:
            raise ValueError("Invalid collision type!")

        if length <= 0:
            raise ValueError("Invalid length!")

        # Creating map
        self.lijst = []
        for i in range(length):
            self.lijst.append(None)
        # If linked lists are used, fill every position with an empty link
        if collision_type == SEPARATE_CHAINING:
            for i in range(length):
                new_link = AdtDoublyLinkedList()
                self.lijst[i] = new_link

    def is_empty(self):
        """ Checks if the list is empty.

        :return: True if list is empty, false otherwise
        """
        for item in self.lijst:
            if self.collision_type == SEPARATE_CHAINING:
                if not item.is_empty():
                    return False
            elif item is not None:
                return False
        return True

    def __len__(self):
        """ Gets the length of the hashmap.

        :return: Length of the hashmap
        """
        return self.length

    def __setitem__(self, search_key, data):
        """ Inserts a new element in the table.

        :param search_key: The new item to insert.
        :param data: The data that needs to be stored.
        """
        # Calculate address and make datanode
        adres = self._calculate_address(search_key)
        new_node = _DataNode(search_key, data)
        # Collision can't occur with separate chaining
        if self.collision_type == SEPARATE_CHAINING:
            self.lijst[adres][0] = new_node
        else:
            # Check if a collision occurs
            if self.lijst[adres] is not None:
                self._solve_collision(adres, new_node)
            else:
                self.lijst[adres] = new_node

    def _calculate_address(self, search_key):
        """ Calculates the adres with the hashfunction.

        :param search_key: The key to be used in the function
        :return: The adres calculated by the hash function.
        """
        adres = 0
        if isinstance(search_key, str):
            adres = len(search_key) % self.length #TODO __HASH__
        elif isinstance(search_key, int):
            adres = search_key % self.length
        return adres

    def __getitem__(self, search_key):
        """ Returns an item from the hashmap.

        :param search_key: The item to search for and return.
        :raise KeyError if the searchkey is not in the hashmap.
        :return: The data linked with the search_key
        """
        if self.is_empty():
            raise KeyError("Hashmap is empty!")
        if self.collision_type == SEPARATE_CHAINING:
            datanode = self._seperate_chaining_search(search_key)
            if datanode is None:
                raise KeyError
            else:
                return datanode.data
        pos = self._find(search_key)
        if pos is None:
            raise KeyError("Hashmap does not contain given search key!")
        else:
            return self.lijst[pos].data

    def __delitem__(self, search_key):
        """ Deletes item from hashmap.

        :param search_key: Key from the node that needs to be deleted.
        :raise KeyError if the searchkey is not in the hashmap.
        """
        if self.is_empty():
            raise KeyError("Hashmap is empty!")
        if self.collision_type == SEPARATE_CHAINING:
            # Exception is raised in function itself if key is not in map
            self._separate_chaining_delete(search_key)
            return
        pos = self._find(search_key)
        if pos is None:
            raise KeyError("Hashmap does not contain given search key!")
        else:
            self.lijst[pos] = None

    def __contains__(self, search_key):
        """ Finds data with a given searchkey in the map.

        :param search_key: Key from the node that has to be found.
        :return: True if the searchkey is in the map, false otherwise.
        """
        if self.collision_type == SEPARATE_CHAINING:
            pos = self._seperate_chaining_search(search_key)
        else:
            pos = self._find(search_key)
        if pos is None:
            return False
        else:
            return True

    def _find(self, search_key):
        """ Finds the position with a given searchkey.

        :param search_key: The key to find in the hashmap
        :return: The position of the data or None
        """
        adres = self._calculate_address(search_key)
        if self.collision_type == LINEAR_PROBING:
            pos = self._linear_probing_search(adres, search_key)
        else:
            pos = self._quadratic_probing_search(adres, search_key)
        return pos

    def _solve_collision(self, adres, data):
        """ Solves a collision by choosing from one of the methods.

        :param adres: Address that caused collision
        :param data: The item to be inserted.
        """
        if self.collision_type == LINEAR_PROBING:
            self._linear_probing(adres, data)
        elif self.collision_type == QUADRATIC_PROBING:
            self._quadratic_probing(adres, data)

    def _linear_probing(self, adres, node):
        """ Solve a collision with linear probing.

        :param adres: Address that caused collision.
        :param node: The node (with searchkey and data) to be inserted.
        :raise MemoryError if the hashmap is full.
        """
        current_adres = adres
        count = 0
        while True:
            # Insert element
            if self.lijst[current_adres] is None:
                self.lijst[current_adres] = node
                break

            current_adres += 1
            count += 1

            if count == self.length:
                raise MemoryError("Hashmap is full!")

            # Make sure to keep looping over the list
            if current_adres == self.length:
                current_adres = 0

    def _linear_probing_search(self, adres, key):
        """ Searches in the map for a given key.

        :param adres: The address that as calculated for that searchkey.
        :param key: The searchkey of the item that needs to be found.
        :return: The address if the key matched an element from the list, None otherwise.
        """
        count = 0
        while True:
            # Search through the list for the searchkey
            if self.lijst[adres] is not None:
                if self.lijst[adres].search_key == key:
                    return adres
            adres += 1
            count += 1
            if count == self.length:
                return None

            # Make sure to keep looping over the list
            if adres == self.length:
                adres = 0

    def _quadratic_probing(self, adres, node):
        """ Solve a collision with quadratic probing.

        :param adres: Address that caused collision.
        :param node: The item to be inserted.
        """
        current_adres = adres
        # We put i on 2 because 0**2 is already checked before increment
        i = 1
        count = 0
        while True:
            # Search through the list for the searchkey
            if self.lijst[current_adres] is None:
                self.lijst[current_adres] = node
                break
            current_adres = (adres + i**2)
            i += 1
            count += 1
            # Check if the whole list was checked
            if count == self.length:
                raise MemoryError("Hashmap is full!")
            # Make sure to keep looping over the list
            if current_adres >= self.length:
                current_adres = current_adres % self.length

    def _quadratic_probing_search(self, adres, key):
        """ Searches in the map for a given key.

        :param adres: The address that as calculated for that searchkey.
        :param key: The searchkey of the item that needs to be found.
        :return: The address of the found item or None.
        """
        current_address = adres
        i = 1
        counter = 0
        while True:
            if self.lijst[current_address] is not None:
                if self.lijst[current_address].search_key == key:
                    return current_address
            current_address = (adres + i**2)
            i += 1
            counter += 1
            # Check if the whole list was checked
            if counter == self.length:
                return None
            # Make sure to keep looping over the list
            if current_address >= self.length:
                current_address = current_address % self.length

    def _separate_chaining_delete(self, search_key):
        """ Deletes a node in the table.

        :param search_key: The key of the node that needs to be deleted
        :raise KeyError if the key does not occur in the list
        """
        adres = self._calculate_address(search_key)
        double_list = self.lijst[adres]
        for i in range(len(double_list)):
            if double_list[i].search_key == search_key:
                del double_list[i]
                return
        raise KeyError

    def _seperate_chaining_search(self, key):
        """ Searches for an element in the hashmap.

        :param key: The searchkey of the element to find.
        :return: Node if item is found, None if not.
        """
        adres = self._calculate_address(key)
        double_list = self.lijst[adres]
        for i in range(len(double_list)):
            if double_list[i].search_key == key:
                return double_list[i]
        return None

    def __repr__(self):
        """
        Generates a string for dot file and visual representation.
        """
        text = ""
        if not self.is_empty():
            text += "digraph hmp {\n"
            text += "node [shape = record];\n"
            if self.collision_type == SEPARATE_CHAINING:
                # Make table
                text += "struct [label=\"{"
                for k in range(len(self)-1):
                    text += "<f" + str(k) + ">"
                    text += ""
                    text += "|"
                text.strip("|")
                text += "}\"];\n"

                # Make nodes
                for i in range(len(self)):
                    if not self.lijst[i].is_empty():
                        for j in range(len(self.lijst[i])):
                            text += "node" + str(i) + str(j) + " [label=\""
                            key = self.lijst[i][j].search_key
                            data = self.lijst[i][j].data
                            text += str(key) + ": " + str(data)
                            text += "\"];\n"
                # Add links
                for i in range(len(self)):
                    if not self.lijst[i].is_empty():
                        text += "struct:f" + str(i) + " -> " + "node" + str(i) + "0;\n"
                        for j in range(1, len(self.lijst[i])):
                            text += "node" + str(i) + str(j-1) + " -> " + "node" + str(i) + str(j) + ";\n"

            else:
                text += "struct [label=\"{"
                for i in range(len(self)):
                    if self.lijst[i] is None:
                        text += ""
                    else:
                        text += str(self.lijst[i].search_key) + ": " + str(self.lijst[i].data)
                    text += "|"
                text.strip("|")
                text += "}\"];\n"
            text += "}"
        return text

    def get_collision_type(self):
        """ Gets the collision type of the hashmap.

        :return: The collision type. Linear probing(0), Quadratic probing(1) and Separate Chaining(2)
        """
        return self.collision_type