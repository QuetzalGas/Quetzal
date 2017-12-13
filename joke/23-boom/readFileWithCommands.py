from twoThreeTree import TwoThreeTree, TreeItem

"""
Volgende stukje code houdt zich bezig met het inlezen van het ingegeven .txt bestand. Wanneer er in het 
.txt bestand 'type=23' staat doet het de gewilde bewerkingen op de boom, die initieel volledig leeg is.
"""
inputFile = open("adt.txt", 'r')            # Het bestand dat ingelezen wordt
listOfLines = inputFile.readlines()         # ListOfFiles is nu een lijst met daarin de lijnen van het bestand
doSomething = 0                             # doSomething zal op 1 staan, wanneer de lijnen in het bestand gericht zijn
                                            # naar een 23-boom (en geen bst bv)
tree = TwoThreeTree()                       # de 23-boom waarmee gewerkt wordt, deze zal volledig leeg worden gemaakt
                                            # (ipv dat er een nieuwe boom wordt aangemaakt) wanneer er een nieuwe boom in het bestand wordt aangemaakt
bestandNummer = 1                           # Zorgt ervoor dat de naam van het .dot bestand steeds veranderd

# Er wordt over alle lijnen in ListOfLines geïtereerd en steeds gekeken of de lijn begint met 'type' -> in dit geval
# wordt er een nieuwe boom aangemaakt (23-boom of een andere, is niet van belang), want als er een huidige boom is,
# dan wordt deze terug leeg gemaakt. Het laatste if-statement zorgt in het geval het 'type=23' is, dat er effectief
# (terug) bewerkingen met 'tree' gebeuren.
# doSomething wordt steeds op 1 gezet als de lijn 'type=23' is, op deze manier wordt aan het 2e if-statement voldaan
# en kunnen de volgende lijnen als deze overeenkomen met 'insert', 'delete' of 'print' worden uitgevoerd.
for line in listOfLines:
    if doSomething == 1 and line[:4] == "type":     # Als er terug een commando voor een nieuwe boom wordt gegeven,
                                                    # kan de huidige opgeruimd worden
        doSomething = 0                             # terug op 0 zodat slechts de boom wordt aangepast als er effectief een nieuwe 'type=23' oproep is
        tree.destroy()                              # maak de boom leeg, zodat er terug vanaf 0 een boom kan opgebouwd worden
    if doSomething == 1:                                    # doSomething == 1, DUS tijd voor actie!
        # check welk het commando is (als het geen commando is, bv. een comment: "# ik ben een comment" dan wordt er niets gedaan)
        if line[:6] == "insert":
            treeNode = TreeItem('?', int(line[7:-1]))       # [7:-1] omdat bij 7 het getal begint/staat en men tot 2 characters
                                                            # tot het einde moet gaan, want de laatste twee zijn: "\n"
            tree.insert(treeNode)                           # de effectieve actie uitvoeren,
        elif line[:6] == "delete":                          # analoog aan insert, alleen moet er geen treeItem worden aangemaakt
            tree.remove(int(line[7:-1]))
        elif line[:5] == "print":
            # commando is print, dus maak de dotfile aan zodat er een png afbeelding van gemaakt kan worden:
            tree.createDotFile("23-" + str(bestandNummer) + ".dot")
            bestandNummer += 1                              # verhogen zodat de volgende print niet dezelfde bestandsnaam krijgt
    if line[:7] == "type=23" and line[:8] != "type=234":                       # in dit geval moet er dus iets gedaan worden met de 23-boom
        doSomething = 1
