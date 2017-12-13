from queue import queue
from ketting import Node, circulaire_ketting
from binaireZoekboom import TreeItem, BinarySearchTree

#TESTEN VOOR CIRCULAIRE GELINKTE KETTING

#nodes aanmaken
a = Node("sup bro?")
b = Node("heyoo")
c = Node("wubba lubba dub dub")
d = Node("42")
e = Node("Zura janai, Katsura da.")
f = Node("Pickle Riiiiick")
g = Node("Glip glop")

#circulaire ketting aanmaken
listy = circulaire_ketting()

#tests
print("CIRCULAIR GELINKTE KETTING")
print("Lege ketting? ", listy.isEmpty())
print("a insert  ", listy.insert(1, a))
print("b insert  ", listy.insert(1, b))
print("c insert  ", listy.insert(1, c))
print("c insert  ", listy.insert(2, d))
print("c insert  ", listy.insert(4, e))
print("f insert  ", listy.insert(1, f))

#het laatst toegvoegde item hoort vanboven te staan, en vervolgens van eerst toegevoegde item naar voorlaatst toegevoegde item
print("\n \nPrint de lijst(ketting):")
listy.print()

print("\nretrieve 3  ", listy.retrieve(3))
print("Item waar head naar wijst:  ", listy.head.next.item, "\n")
print("delete 1  ", listy.delete(1), "\n")
print("Nieuw eerste item :  ", listy.head.next.item, "\n")
print("\nPrint van de ketting:")
listy.print()
print("\n \n \n")


#TESTEN VOOR QUEUE

#queue aanmaken en enkele items invoegen
que = queue()
que.enqueue(5)
que.getFront()
que.enqueue(6)
que.enqueue(12)
que.enqueue(13)
que.enqueue(14)
que.enqueue("Grandpa Rick, can you help me with my science homework?")
que.enqueue("Yeah, just don't do it.")

#uittesten hoe de queue verandert:
print("QUEUE \nNa alle items toevoegen")
que.print()
print("queueFront:  ", que.getFront(), "\n")

que.dequeue()
print("\nNa dequeue:")
que.print()
print("queueFront (bool, front):  ", que.getFront(), "\n")

print("\nNa nog een keer dequeue:")
que.dequeue()
que.print()
print("queueFront (bool, front):  ", que.getFront())

print("\nEnqueue met 'WoWeeee!':")
que.enqueue("WoWeeee!")
que.print()


#BINAIRE ZOEKBOOM

#nodes aanmaken
a = TreeItem('a', 5)
b = TreeItem('b', 3)
c = TreeItem('c', 8)
d = TreeItem('d', 2)
e = TreeItem('e', 4)
f = TreeItem('f', 7)
g = TreeItem('g', 1)

#BST aanmaken
ai = BinarySearchTree(a)

#tests
print("\n\nBINAIRE ZOEKBOOM\nLeeg (ja):  ", ai.isEmpty())
ai.searchTreeInsert(b)
print("c insert  ", ai.searchTreeInsert(c))
ai.searchTreeInsert(d)

#test subtrees
oui = ai.left
non = oui.left
print("\nSubtree test:\noui.root.key  ", oui.root.key)
print(oui.left.root.key, "\n \n")

print("ai.retrieve  ", ai.searchTreeRetrieve(5))


ai.searchTreeInsert(e)
ai.searchTreeInsert(f)
print("\n \ninsert g  ", ai.searchTreeInsert(g), "\n")
ai.inorderTraverse()
print("\nRetrieve key=1  ", ai.searchTreeRetrieve(1))

ai.searchTreeInsert(e)
ai.searchTreeInsert(f)
print("\n \n", ai.searchTreeInsert(g), "\n")
ai.inorderTraverse()
print("\n", ai.searchTreeRetrieve(1))
print("\nInorder traverse")
ai.print()