# Joke Duwaerts, Binaire zoekboom


class _TreeItem:
    def __init__(self, key, item):
        self.item = item
        self.key = key


class AdtBinarySearchTree:
    def __init__(self, root=None, left=None, right=None, parent=None):
        """
        Een nieuwe binaire boom wordt geïnitialiseerd.
        :param root: de wortel van de binaire zoekboom
        :param left: het linkerkind van de boom, dat oftewel None is, oftewel ook een binaire zoekboom
        :param right: het rechterkind: oftewel None oftewel ook binaire zoekboom
        :param parent: Elke BST heeft een parent, behalve als in de root de eigenlijke wortel van de gehele BST zit, deze heeft geen parent.
        """
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

    def destroy(self):
        self.root = None
        self.right = None
        self.left = None

    def is_empty(self):
        """
        Checkt of de binaire boom leeg is.
        :return: geeft True indien leeg, False indien niet leeg.
        """
        if (self.left is None) and (self.right is None):
            return True
        else:
            return False

    def table_is_empty(self):
        return self.root is None

    def insert(self, key, item):
        self.search_tree_insert(_TreeItem(key, item))

    def search_tree_insert(self, item):
        """
        Voegt nieuwe TreeNode toe aan binaire zoekboom, op de juiste plaats, als er nog geen item met dezelfde zoeksleutel aanwezig is.
        :param item: een TreeNode
        :return: geeft True indien de zoeksleutel van de TreeNode nog niet aanwezig was,
                 geeft False indien het wel al aanwezig was.
        """
        if self.root is None and self.parent is None:
            self.root = item
            return

        if item.key < self.root.key:
            # Als de key van item kleiner is dan de key van de root,
            if self.left is None:
                # en de linkerdeelboom is leeg,
                # maak dan een nieuwe BinarySearchTree aan met als root 'item'.
                self.left = AdtBinarySearchTree(item)
                # Deze nieuwe BST heeft als ouder de huidige BST.
                self.left.parent = self
                return True
            else:
                # Als er al een linkerkind was, zoek dan verder naar een plaats
                # bij dat linkerkind.
                return self.left.search_tree_insert(item)
        elif item.key > self.root.key:
            # Zelfde logica als hierboven.
            if self.right is None:
                self.right = AdtBinarySearchTree(item)
                self.right.parent = self
                return True
            else:
                return self.right.search_tree_insert(item)

        if item.key == self.root.key:
            # Als item.key == de key van de root, dan is er dus al een node met deze key
            # en moet er geen nieuwe worden toegevoegd, geeft False terug.
            return False

    def search_tree_retrieve(self, key, subtree=False):
        """
        Indien een item met de gevraagde zoeksleutel aanwezig is, wordt de root (TreeNode) OF (sub)binaire zoekboom met de zoeksleutel teruggegeven.
        :param key: de zoeksleutel, waar naar wordt gezocht.
        :param subtree: Als deze op True wordt gezegd, wordt een subtree teruggeven en geen TreeNode, dit wordt gebruikt bij de
                        remove functie.
        :return: geeft de (sub) binaire boom terug als er een TreeNode met de zoeksleutel aanwezig is, anders geeft het False terug
        """
        if (self.root is None) and (self.parent is None):
            return (False, None)
        # als key kleiner is dan de key van de root, zoek dan verder in de
        if key < self.root.key and self.left is not None:
            # linkerdeelboom, als deze aanwezig is.
            return self.left.search_tree_retrieve(key, subtree)
        # als key groter is dan de key van de root, zoek dan verder in de
        elif key > self.root.key and self.right is not None:
            # rechterdeelboom, als deze aanwezig is.
            return self.right.search_tree_retrieve(key, subtree)
        # Als key == de key van de root, geef dan True door en...
        if key == self.root.key:
            if subtree:
                # ...de subtree, in het geval we een subtree terug willen. (subtree=True)
                return (True, self)
            # ...de TreeNode, in het algemene geval.
            return (True, self.root)
        else:
            # De key is niet teruggevonden, geef False terug en None.
            return (False, None)

    def inorder_traverse(self):
        """
        Bezoekt de nodes van de BST volgens inorder traverse volgorde. Geeft een lijst van de rootItems in deze volgorde terug.
        """
        list_inorder = list()

        if self.left is not None:
            # Verleng de huidige lijst met de lijst van de linkerdeelboom
            list_inorder = list_inorder + self.left.inorder_traverse()

        # voeg het root.item er vervolgens aan toe
        list_inorder.append(self.root.item)

        if self.right is not None:
            # Verleng de huidige lijst met de lijst van de rechterdeelboom
            list_inorder = list_inorder + self.right.inorder_traverse()

        return list_inorder

    def inorder_successor(self, right_child):
        """
        Geeft de inorder successor terug. Zoekt dus naar het meest linkse kind in de rechterdeelboom van de node (rightChild).
        Préconditie : node heeft een rechterkind (dit rechterkind wordt ingegeven, niet de node zelf)
        :param node: de knoop waarvan men de inorder successor wilt vinden
        :return: de inorder successor
        """
        if right_child.left is not None:
            # rightChild heeft nog een linkerkind, ga dan zoeken naar een linkerkind bij dat kind
            return self.inorder_successor(right_child.left)
        else:
            # geen linkerkind meer, dan is de huidige subtree de inorder
            # successor
            return right_child

    def act_remove(self):
        """
        Verwijdert de knoop (of juister: een _TreeItem dat in de root zit van de (sub)tree.
        """
        if self.parent:                             # als node niet wortel is, dus WEL een parent heeft:
            # en ze is leeg, dan moet de parent op de plaats van de node geen
            # kind meer hebben.
            if self.is_empty() is True:
                if self.parent.left == self:        # Bepaal of node het linker- of rechterkind is en zet dan het juiste kind van
                    self.parent.left = None  # de parent op None.
                else:
                    self.parent.right = None

        if (self.left is None) and self.right:
            # Als node maar één kind heeft, een rechterkind:
            # stap 1: Plaats dan in de root de root van het rechterkind
            self.root = self.right.root
            # stap 2: Neem de kinderen van dat rechterkind over
            self.left = self.right.left
            self.right = self.right.right
        elif (self.right is None) and self.left:
            # Als node maar één kind heeft, een linkerkind
            # stap 1: Plaats dan in de root de root van het linkerkind
            self.root = self.left.root
            # stap 2: Neem de kinderen van dat linkerkind over
            self.right = self.left.right
            self.left = self.left.left
        if self.left and self.right:
            # Als node twee kinderen heeft, zoek dan de inorder succesor,
            inorderSucc = self.inorder_successor(self.right)
            # plaats de root van deze succ in de huidige root en
            self.root = inorderSucc.root  
            # zorg dat deze inorder successor verwijderd wordt.
            inorderSucc.act_remove()

        # zorg er voor dat de kinderen die verplaatst zijn, allemaal de juiste parent krijgen
        #   (maw dat ze 'weten' dat de huidige (sub)tree de parent is).
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def remove(self, key):
        """
        Verifieert of de zoeksleutel voorkomt in de boom. Zo ja, dan gaat het effectieve verwijderen door in act_remove.
        :param key: de zoeksleutel van de knoop die verwijderd moet worden
        :return: Als key voorkomt geeft resultaat terug van het verwijderen (act_remove).
                         niet voorkomt geeft het False terug.
        """
        (bool, subtree) = self.search_tree_retrieve(key, True)

        # True wordt bijgevoegd bij de parameterlijst van de retrievefunctie
        # dit wil zeggen dat we een subtree terug willen krijgen en geen
        # _TreeItem
        if bool is False:
            return False
        else:
            # key komt voor, dus voer het verwijderen effectief uit
            return subtree.act_remove()

    def print(self):
        """
        Print de zoeksleutels van de TreeNodes in inorder_traverse.
        """

        # Bezoek eerst het linkerkind, als aanwezig
        if self.left is not None:       
            self.left.print()

        # Dan de eigen root
        print(self.root.key)            

        # En vervolgens het rechterkind, als aanwezig
        if self.right is not None:      
            self.right.print()
