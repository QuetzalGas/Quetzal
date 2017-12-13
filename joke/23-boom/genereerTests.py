from twoThreeTree import TreeItem, TwoThreeTree
import random
from datetime import datetime
from time import sleep

"""
Ik heb eerst kleinere bomen getest, toen er nog frequent bugs waren. Toen deze weg leken te zijn heb ik de volgende twee 
functies gemaakt. In removing() laat ik in de loop zelf het .dot bestand maken. Dit is een extra check, omdat er dan 
steeds door heel de boom wordt getraversed. (als er dus iets mis is, is de kans groot dat de createDotFile functie het 
gemerkt heeft, want deze vraagt zowal kinderen, roots als parent op en checkt dus eigenlijk de hele boom.)
Ik heb het een paar keer met 300 TreeItems en dus 299 removes uitgetest.
"""

def genereerBoom(aantal):
    """
    Deze functie maakt een boom aan met 'aantal' TreeItems.
    :param aantal: geeft het aantal TreeItems.
    :return: geeft een TwoThreeTree terug.
    """
    # Er wordt een lijst aangemaakt met daarin TreeItems met zoeksleutel steeds 1 groter dan de zoeksleutel van de vorige
    #  die in de lijst werd geplaatst. Uit deze lijst wordt random een TreeItem gekozen en in de vers aangemaakte 23B-boom
    # geplaatst. Het geplaatste item wordt verwijderd uit de lijst, zodat zeker alle items in de boom zijn geplaatst wanneer
    # het einde van de loop wordt bereikt.
    lijstMetTreeItems = list()
    for i in range(aantal):
        lijstMetTreeItems.append(TreeItem(str(i), i))       # Invoegen TreeItems met zoeksleutel 'i' en item de string van 'i'
    tree = TwoThreeTree()
    size = aantal                                           # Bepaalt hoe veel keer de loop wordt gedaan
    for i in range(size):
        random.seed(datetime.now())                         # Om ervoor te zorgen dat de seed steeds veranderd naargelang de tijd
        randomInLijst = random.randint(0, aantal - 1)       # RandomInLijst is de index voor de lijst die random werd gekozen
        item = lijstMetTreeItems[randomInLijst]             # item is nu het TreeItem dat op de random index in LijstMetTreeItems zat
        del lijstMetTreeItems[randomInLijst]                # Het Item op die index wordt verwijderd om overbodige inserts
                                                            # (voor de tests) te vermijden en ervoor te zorgen dat alle Treeitems in
                                                            # de boom worden geplaatst
        tree.insert(item)                   # Het TreeItems plaatsen in de boom
        aantal -= 1                         # Aantal = aantal - 1, omdat er 1 TreeItem minder in de lijst is, zodat de randomwaarde
                                            # in de volgende loop in het juiste interval wordt gekozen
    tree.createDotFile("treeWhole.dot")     # Een .dot file wordt aangemaakt, dan kan de 23-boom nagekeken worden
    return tree

def removing(tree, aantal):
    """
    Verwijderd alle TreeItems, behalve 1 uit de boom. Er wordt 1 overgelaten om te checken of alles zeker oké is.
    :param tree:    De 23-boom waarvan men de TreeItems gaat verwijderen.
    :param aantal:  Het aantal items in de 'tree'.
    """
    # Een lijst wordt aangemaakt met hierin: 1,2,...,aantal
    lijstMetKeys = list()
    for i in range(aantal):
        lijstMetKeys.append(i)

    # Size wordt gebruikt voor de loop, om alle TreeItems, behalve 1 (aantal - 1) te verwijderen uit 'tree'.
    size = aantal - 1

    # Er wordt steeds random uit de lijst een getal gekozen, dit getal zal dan als key-waarde worden gebruikt dat moet worden
    # verwijderd uit 'tree'. Ook hier wordt het gebruikte element uit de lijst verwijderd, zodat zeker alle TreeItems behalve
    # één verwijderd worden.
    for i in range(size):
        random.seed(datetime.now())
        randomInLijst = random.randint(0, aantal - 1)
        key = lijstMetKeys[randomInLijst]
        del lijstMetKeys[randomInLijst]
        aantal -= 1
        tree.remove(key)
        tree.createDotFile("treeNotSoWhole.dot")

##### Testen met 200 TreeItems #########################################################################################
tree1 = genereerBoom(300)
removing(tree1, 300)

# error:  26
# Voor random.seed() heb ik volgende webpagina geraadpleegd op 7/12/2017:
# https://stackoverflow.com/questions/27276135/python-random-system-time-seed