# from Stack import Stack
# from CircularLinkedList import CircularLinkedList
# from BinarySearchTree import BinarySearchTree
from TwoThreeFourTree import TwoThreeFourTree
from TwoThreeFourTree import TreeItem


# def createStack(instructions, teller):
#     s = Stack()
#     instructions = instructions[1:]
#     for i in instructions:
#         j = i.split(" ")
#         if j[0] == "insert":
#             s.push(j[1])
#         elif j[0] == "delete":
#             s.pop()
#         elif j[0] == "print":
#             st = ""
#             elements = []
#             while s.getTop()[1]:
#                 elements.append(s.pop()[0])
#             filename = "stack-"+str(teller)+".dot"
#             with open(filename, "w") as file:
#                 file.write("digraph G {\ngraph [\nrankdir = \"LR\"\n];\n\n\"node\" [\nlabel = \"")
#                 for k in elements:
#                     st += str(k)
#                     st += "|"
#                 st = st.strip("|")
#                 file.write(st)
#                 file.write("\"\nshape = \"record\"\n];\n}")

# def createLinkedList(instructions, teller):
#     s = CircularLinkedList()
#     instructions = instructions[1:]
#     for i in instructions:
#         j = i.split(" ")
#         if j[0] == "insert":
#             s.insert(int(j[2]), j[1])
#         elif j[0] == "delete":
#             s.delete(int(j[1]))
#         elif j[0] == "print":
#             elements = []
#             for i in range(s.getLength()):
#                 elements.append(s.retrieve(i+1)[0])
#             filename = "ll-"+str(teller)+".dot"
#             with open(filename, "w") as file:
#                 file.write("digraph G {\ngraph [\nrankdir = \"LR\"\n];\n\n")
#                 for k in range(len(elements)):
#                     st = str(k)+" [\nlabel = \""+str(elements[k])+"\"\nshape = \"record\"\n];\n\n"
#                     file.write(st)
#                 # if len(elements) != 0:
#                 st = ""
#                 for k in range(len(elements)):
#                     st += str(k)
#                     st += " -> "
#                 st = st.strip(" -> ")
#                 file.write(st)
#                 file.write("\n}")

# def createBinarySearchTree(instructions, teller):
#     s = BinarySearchTree()
#     instructions = instructions[1:]
#     for i in instructions:
#         j = i.split(" ")
#         if j[0] == "insert":
#             s.searchTreeInsert(j[1])
#         elif j[0] == "delete":
#             # s.searchTreeDelete(j[1])
#             pass
#         elif j[0] == "print":
#             elements = []
#             for i in range(s.getLength()):
#                 elements.append(s.retrieve(i + 1)[0])
#             filename = "ll-" + str(teller) + ".dot"
#             with open(filename, "w") as file:
#                 file.write("digraph G {\ngraph [\nrankdir = \"LR\"\n];\n\n")
#                 for k in range(len(elements)):
#                     st = str(k) + " [\nlabel = \"" + str(elements[k]) + "\"\nshape = \"record\"\n];\n\n"
#                     file.write(st)
#                 # if len(elements) != 0:
#                 st = ""
#                 for k in range(len(elements)):
#                     st += str(k)
#                     st += " -> "
#                 st = st.strip(" -> ")
#                 file.write(st)
#                 file.write("\n}")

def createTwoThreeFourTree(instructions, teller):
    s = TwoThreeFourTree()
    instructions = instructions[1:]
    for i in instructions:
        j = i.split(" ")
        if j[0] == "insert":
            newTreeItem = TreeItem(int(j[1]),int(j[1]))
            s.tableInsert(newTreeItem)
        elif j[0] == "delete":
            s.tableDelete(int(j[1]))
            pass
        elif j[0] == "print":
            filename = "234-" + str(teller) + ".dot"
            with open(filename, "w") as file:
                file.write("digraph G {\ngraph [\nrankdir = \"RR\"\n];\n\n")
                file.write(s.dot(s.root, 1, ""))
                file.write("}")


filename = input("Filename: ")
f=open(filename,"r")

types = ["stack", "queue", "bst", "ll", "23", "234", "rb", "hlin", "hquad", "hsep", "heap"]
graphs = []
newGraph = []
for line in f:
    if line[0] != "#" and line[0] != "\n":
        line = line.strip()
        split = line.split("=")
        for i in split:
            if i == "type":
                k = 0
                for j in types:
                    if split[1] == j:
                        type = k
                    k += 1
                graphs.append(newGraph)
                newGraph = []
                newGraph.append(type)
            elif i not in types:
                newGraph.append(i)
graphs.append(newGraph)

stackTeller = llTeller = TTFTeller = 0
for k in graphs:
    for j in k:
        if j == 5:
            TTFTeller += 1
            createTwoThreeFourTree(k, TTFTeller)
        # elif j == 0:
        #     stackTeller += 1
        #     createStack(k,stackTeller)
        # elif j == 3:
        #     llTeller += 1
        #     createLinkedList(k,llTeller)




