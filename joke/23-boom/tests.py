from twoThreeTree import TwoThreeTree, TreeItem

"""
Hieronder zijn tests die ik heb gedaan, deze heb ik tijdens het implementeren gebruikt.
De uiteindelijke grotere test zijn te vinden in 'genereerTests.py'
De eerste tests had ik gemaakt toen ik nog niet met .dot (en pydot) werkte, daar had ik toen inorder traverse voor gebruikt.
Ik heb tijdens het schrijven van de code gebruik gemaakt van print() om te checken wat er gebeurde, deze heb ik nu echter wel 
verwijderd in het "nette" bestand (er is nog een "klad" bestand dat ik gebruikte om nog bugs te vinden).
"""

item0 = TreeItem('0', 0)
item1 = TreeItem('1', 1)
item2 = TreeItem('2', 2)
item3 = TreeItem('3', 3)
item4 = TreeItem('4', 4)
item5 = TreeItem('5', 5)
item6 = TreeItem('6', 6)
item7 = TreeItem('7', 7)
item8 = TreeItem('8', 8)
item9 = TreeItem('9', 9)
item10 = TreeItem('10', 10)
item11 = TreeItem('11', 11)
item12 = TreeItem('12', 12)
item13 = TreeItem('13', 13)
item14 = TreeItem('14', 14)
item15 = TreeItem('12', 15)
item17 = TreeItem('13', 17)
item18 = TreeItem('14', 18)
item16 = TreeItem('14', 16)
item19 = TreeItem('14', 19)
item20 = TreeItem('20', 20)
item21 = TreeItem('21', 21)
item22 = TreeItem('22', 22)
item23 = TreeItem('23', 23)
item24 = TreeItem('24', 24)
item25 = TreeItem('25', 25)
item26 = TreeItem('26', 26)

# TEST INSERT =================================================================================================================
myboom = TwoThreeTree()
myboom.insert(item5)
print("\n\nInsert 5\nDe root van de boom, na 1 insert: item5 (key = 5):  ", myboom.rootLeft.key)
print("Print na 1 insert (5):")
myboom.printInorder()

myboom.insert(item3)
print("\n\nInsert 3\nDe root van de boom, na 2 inserts: item5, item3:  linkerroot: ", myboom.rootLeft.key, "  rechterroot: ", myboom.rootRight.key)
print("Print na 2 inserts (5, 3):")
myboom.printInorder()

myboom.insert(item8)
print("\n\nInsert 8\nDe root van de boom, na 3 inserts: item5, item3, item8:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: linkerkind", myboom.left.rootLeft.key, " mid: ", myboom.rootMid, " right: ", myboom.right.rootLeft.key)
print("Print na 3 inserts (5, 3, 8):")
myboom.printInorder()
print(myboom.left)

myboom.insert(item1)
print("\n\nInsert 1\nDe root van de boom, na 4 inserts: item5, item3, item8, item1:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: linkerkind (kleine value:)", myboom.left.rootLeft.key, " linkerkind grote value:)", myboom.left.rootRight.key, " mid: ", myboom.rootMid, " right: ", myboom.right.rootLeft.key)
print("Print na 4 inserts (5, 3, 8, 1):")
myboom.printInorder()

myboom.insert(item10)
print("\n\nInsert 10: \nDe root van de boom, na 5 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: linkerkind (kleine value:)", myboom.left.rootLeft.key, " linkerkind grote value:)", myboom.left.rootRight.key, " mid: ", myboom.rootMid, " right (kleine value): ", myboom.right.rootLeft.key, "right big value) ", myboom.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10):")
myboom.printInorder()

myboom.insert(item9)
print("\n\nInsert 9: \nDe root van de boom, na 6 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight.key)
print("de kinderen: linkerkind (kleine value:)", myboom.left.rootLeft.key, " linkerkind grote value:)", myboom.left.rootRight.key, " mid: ", myboom.midLeft.rootLeft.key, " right (kleine value): ", myboom.right.rootLeft.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9):")
myboom.printInorder()

myboom.insert(item7)
print("\n\nInsert 7: \nDe root van de boom, na 7 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight.key)
print("de kinderen: linkerkind", myboom.left.rootLeft.key, myboom.left.rootRight.key, " mid: ", myboom.midLeft.rootLeft.key, myboom.midLeft.rootRight.key, " right ", myboom.right.rootLeft.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7):")
myboom.printInorder()

myboom.insert(item11)
print("\n\nInsert 11: \nDe root van de boom, na 8 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight.key)
print("de kinderen: linkerkind", myboom.left.rootLeft.key, myboom.left.rootRight.key, " mid: ", myboom.midLeft.rootLeft.key, myboom.midLeft.rootRight.key, " right ", myboom.right.rootLeft.key, myboom.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7, 11):")
myboom.printInorder()
print("parent linkerkind, en rechterkind ", myboom.left.parent.rootLeft.key, myboom.right.parent.rootRight.key)

myboom.insert(item6)
print("\n\nInsert 6: \nDe root van de boom, na 9 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: left", myboom.left.rootLeft.key, myboom.right.rootLeft.key)
print("kinderen van linkerkind links", myboom.left.left.rootLeft.key, myboom.left.left.rootRight.key, " rechts ", myboom.left.right.rootLeft.key)
print("kinderen van rechterkind links: ", myboom.right.left.rootLeft.key, " rechts ", myboom.right.right.rootLeft.key, myboom.right.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7, 11, 6):")
myboom.printInorder()

myboom.insert(item4)
print("\n\nInsert 4: \nDe root van de boom, na 10 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: left", myboom.left.rootLeft.key,"-", myboom.left.rootRight.key, "  ", myboom.right.rootLeft.key)
print("kinderen van linkerking links", myboom.left.left.rootLeft.key, myboom.left.midLeft.rootLeft.key, myboom.left.right.rootLeft.key)
print("kinderen van rechterkind links: ", myboom.right.left.rootLeft.key, " rechts ", myboom.right.right.rootLeft.key, "-",myboom.right.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7, 11, 6, 4):")
myboom.printInorder()

myboom.insert(item2)
print("\n\nInsert 2: \nDe root van de boom, na 11 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight)
print("de kinderen: left", myboom.left.rootLeft.key,"-", myboom.left.rootRight.key, "  ", myboom.right.rootLeft.key)
print("kinderen van linkerking links", myboom.left.left.rootLeft.key,"-", myboom.left.left.rootRight.key, myboom.left.midLeft.rootLeft.key, myboom.left.right.rootLeft.key)
print("kinderen van rechterkind links: ", myboom.right.left.rootLeft.key, " rechts ", myboom.right.right.rootLeft.key, "-",myboom.right.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7, 11, 6, 4, 2):")
myboom.printInorder()

myboom.insert(item0)
print("\n\nInsert 0: \nDe root van de boom, na 11 inserts:  linkerroot: ", myboom.rootLeft.key, "middenroot  ", myboom.rootMid, "  rechterroot: ", myboom.rootRight.key)
print(myboom.left.rootLeft.key," ", myboom.midLeft.rootLeft.key, " ",myboom.right.rootLeft.key)
print(myboom.left.left.rootLeft.key, myboom.left.right.rootLeft.key, "  ", myboom.midLeft.left.rootLeft.key, myboom.midLeft.right.rootLeft.key, "  ", myboom.right.left.rootLeft.key, myboom.right.right.rootLeft.key, "-",myboom.right.right.rootRight.key)
print("Print na 4 inserts (5, 3, 8, 1, 10, 9, 7, 11, 6, 4, 2):")
myboom.printInorder()


# TEST RETRIEVE ===============================================================================================================
(retrieve1, subtree1, numb) = myboom.retrieve(5)
print("Retrieve 5 (aanwezig in boom): node.key:", retrieve1.key)

(retrieve2, subtree2, numb) = myboom.retrieve(0)
print("Retrieve 0 (aanwezig in boom): node.key:", retrieve2.key)

(retrieve2, subtree3, numb) = myboom.retrieve(3)
print("Retrieve 3 (aanwezig in boom): node.key:", retrieve2.key)

(retrieve2, subtree4, numb) = myboom.retrieve(11)
print("Retrieve 11 (aanwezig in boom): node.key:", retrieve2.key)


# TEST INORDER SUCCESSOR ======================================================================================================

subtree = subtree1.right.inorderSuccessor()
print("Inorder succ van 5 (6): ", subtree.rootLeft.key)
print("Inorder succ van 7 (8): ", myboom.right.inorderSuccessor().rootLeft.key)
subtree = subtree3.midLeft.inorderSuccessor()
print("Inorder succ van 3 (4): ", subtree.rootLeft.key)

# TEST REMOVE =================================================================================================================

myboom.printInorder()
myboom.remove(4)
myboom.printInorder()

print("         ", myboom.rootLeft.key, "   ", myboom.rootMid, "  ", myboom.rootRight)
print("  ", myboom.left.rootLeft.key, "               ", myboom.right.rootLeft.key, "-", myboom.right.rootRight.key)
print(myboom.left.left.rootLeft.key, "   ", myboom.left.right.rootLeft.key, "      ", myboom.right.left.rootLeft.key, "-", myboom.right.left.rootRight.key," ", myboom.right.midLeft.rootLeft.key, " ", myboom.right.right.rootLeft.key, "-", myboom.right.right.rootRight.key )

myboom.remove(8)
myboom.printInorder()
print("New right-rootRight: ", myboom.right.rootRight.key, "   new right-midleft-rootLeft: ", myboom.right.midLeft.rootLeft.key)

myboom.remove(5)
myboom.printInorder()

myboom.remove(0)
myboom.printInorder()
print("                    ", myboom.rootLeft.key, "   ", myboom.rootMid, "  ", myboom.rootRight)
print("           ", myboom.left.rootLeft.key, "                     ", myboom.right.rootLeft.key, "-", myboom.right.rootRight)
print(myboom.left.left.rootLeft.key,"-", myboom.left.left.rootRight.key, "   ", myboom.left.right.rootLeft.key, "-", myboom.left.right.rootRight, "      ", myboom.right.left.rootLeft.key, "-", myboom.right.left.rootRight," ", myboom.right.midLeft, " ", myboom.right.right.rootLeft.key, "-", myboom.right.right.rootRight )

myboom.remove(7)
myboom.printInorder()
print("in root:  ", myboom.rootLeft.key, "-", myboom.rootRight.key)
print(myboom.left.rootLeft.key,"-", myboom.left.rootRight.key, "  ", myboom.midLeft.rootLeft.key,"-", myboom.midLeft.rootRight, "  ", myboom.right.rootLeft.key )

myboom.remove(10)
myboom.printInorder()
myboom.remove(6)
myboom.printInorder()

myboom.remove(2)
myboom.printInorder()

myboom.remove(9)
myboom.printInorder()
print(" root of tree: ", myboom.rootLeft.key)

myboom.remove(3)
print(myboom.left, myboom.midLeft, myboom.right)
myboom.printInorder()

myboom.remove(1)
myboom.printInorder()

myboom.remove(11)
myboom.printInorder()

######################################################################################################
tree = TwoThreeTree()
tree.insert(item11)
tree.insert(item5)
tree.insert(item8)
tree.insert(item4)
tree.insert(item6)
tree.insert(item3)
tree.insert(item2)
tree.insert(item15)
tree.insert(item12)
tree.insert(item16)
tree.insert(item10)
tree.insert(item9)
tree.insert(item0)
tree.insert(item19)
tree.insert(item17)
tree.insert(item14)
tree.insert(item13)
tree.insert(item18)

treeItem12 = TreeItem("life?", 12)
treeItem18 = TreeItem("Dont talk to me", 18)
treeItem18dup = TreeItem("about life.", 18)
tree.insert(treeItem12)
tree.insert(treeItem18)
tree.insert(treeItem18dup)

print(tree.right.right.rootRight.next.next.item)
tree.remove(12)
tree.remove(12)
tree.createDotFile("23treeVOOR.dot")
tree.remove(18)
tree.remove(18)
tree.remove(18)
# tree.remove(15)
# tree.remove(10)
# tree.remove(11)
# tree.remove(4)
# tree.remove(8)
# tree.remove(5)
# tree.remove(19)
# tree.remove(14)
# tree.remove(16)
# tree.remove(6)
# tree.remove(3)
# tree.remove(13)
# tree.remove(9)
# tree.remove(18)
# tree.remove(2)
# tree.remove(0)
tree.createDotFile("23treeNA.dot")

#############################################################################################
tree2 = TwoThreeTree()
tree2.insert(item4)
tree2.insert(item23)
tree2.insert(item9)
tree2.insert(item21)
tree2.insert(item8)
tree2.insert(item16)
tree2.insert(item14)
tree2.insert(item15)
tree2.insert(item24)
tree2.insert(item3)
tree2.insert(item10)
tree2.insert(item17)
tree2.insert(item20)
tree2.insert(item19)
tree2.insert(item25)
tree2.insert(item12)
tree2.insert(item13)
tree2.insert(item0)
tree2.insert(item22)
tree2.insert(item1)
tree2.insert(item5)
tree2.insert(item6)
tree2.insert(item7)
tree2.insert(item11)

# tree2.remove(13)
# tree2.remove(17)
# tree2.remove(19)
# tree2.remove(10)
# tree2.remove(8)
# tree2.remove(16)
# tree2.remove(14)
# tree2.remove(11)
# tree2.remove(7)
# tree2.remove(6)
# tree2.remove(9)
# tree2.remove(4)
# tree2.printVersionTwo("funny.png")
# tree2.remove(5)
# tree2.printVersionTwo("after.png")


tree2.remove(12)
tree2.remove(15)
tree2.remove(10)
tree2.remove(4)
tree2.remove(11)
tree2.remove(8)
tree2.remove(5)