from quetzal import *
from unittest import TestCase

class TestHashmap(TestCase):
    # tests voor linear probing

    def testLinearProbingFull(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[3] = "test1"
        hashmap[33] = "test2"
        hashmap[23] = "test3"
        hashmap[88] = "test4"
        hashmap[123] = "test5"
        try:
            hashmap[13] = "test6"
        except:
            self.assertTrue(True)


    def testLinearProbing(self):
        hashmap = AdtHashMap(5, 0)
        hashmap.tableInsert(3, "test")
        hashmap.tableInsert(33, "test2")
        self.assertEqual(hashmap.lijst[3].searchKey, 3)
        hashmap.tableInsert("searchkey", "test2")

    def testRetrieveLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap.tableInsert(4, "test")
        self.assertEqual(hashmap.tableRetrieve(4).searchKey, 4)
        self.assertFalse(hashmap.tableRetrieve(5))

    def testDeleteLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap.tableInsert(5, "test")
        self.assertTrue(hashmap.tableDelete(5))
        self.assertFalse(hashmap.tableRetrieve(5))
        self.assertTrue(hashmap.isEmpty())

    def testSolveCollisionLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap.tableInsert(3, "test")
        hashmap.tableInsert(33, "test")
        hashmap.tableInsert(23, "test")
        hashmap.tableInsert(88, "test")
        hashmap.tableInsert(123, "test")
        self.assertFalse(hashmap.tableInsert(13, "test"))

    # tests voor quadratic probing

    def testQuadraticProbingFull(self):
        hashmap = AdtHashMap(5, 1)
        hashmap.tableInsert(2, "test")
        hashmap.tableInsert(7, "test")
        hashmap.tableInsert(5, "test")
        hashmap.tableInsert(15, "test")
        hashmap.tableInsert(25, "test")
        self.assertFalse(hashmap.tableInsert(35, "test"))

    def testQuadraticProbing(self):
        hashmap = AdtHashMap(5, 1)
        hashmap.tableInsert(15, "test")
        hashmap.tableInsert(25, "test")
        self.assertEqual(hashmap.lijst[0].searchKey, 15)
        self.assertEqual(hashmap.lijst[1].searchKey, 25)

    def testRetrieveQP(self):
        hashmap = AdtHashMap(5, 1)
        hashmap.tableInsert(4, "test")
        self.assertEqual(hashmap.tableRetrieve(4).searchKey, 4)

    def testDeleteQP(self):
        hashmap = AdtHashMap(5, 1)
        hashmap.tableInsert(5, "test")
        self.assertTrue(hashmap.tableDelete(5))
        self.assertFalse(hashmap.tableRetrieve(5))
        self.assertTrue(hashmap.isEmpty())

    def testSolveCollisionQP(self):
        hashmap = AdtHashMap(5, 1)
        hashmap.tableInsert(3, "test")
        hashmap.tableInsert(33, "test")
        hashmap.tableInsert(23, "test")
        self.assertFalse(hashmap.tableInsert(88, "test"))
        self.assertEqual(hashmap.lijst[2].searchKey, 23)

    # tests voor seperate chaining

    def testSeperateChainingFull(self):
        hashmap = AdtHashMap(5, 2)
        hashmap.tableInsert(0, "test1")
        hashmap.tableInsert(0, "test2")
        hashmap.tableInsert(0, "test3")
        hashmap.tableInsert(3, "test")
        hashmap.tableInsert(3, "test1")
        self.assertTrue(hashmap.tableInsert(3, "test"))

    def testSeperateChaining(self):
        hashmap = AdtHashMap(5, 2)
        self.assertTrue(hashmap.tableInsert(15, "test"))
        self.assertTrue(hashmap.tableInsert(25, "test"))

    def testRetrieveSC(self):
        hashmap = AdtHashMap(5, 2)
        hashmap.tableInsert(4, "test")
        self.assertEqual(hashmap.tableRetrieve(4).searchKey, 4)

    def testDeleteSC(self):
        hashmap = AdtHashMap(5, 2)
        hashmap.tableInsert(5, "test")
        hashmap.tableDelete(5)
        self.assertTrue(hashmap.isEmpty())

    def testSolveCollisionSC(self):
        hashmap = AdtHashMap(5, 2)
        hashmap.tableInsert(3, "test")
        hashmap.tableInsert(33, "test")
        hashmap.tableInsert(23, "test")
        hashmap.tableInsert(88, "test")
        hashmap.tableInsert(123, "test")
        self.assertTrue(hashmap.tableInsert(3, "test"))

    # algemeen

    def testRetrieveEmpty(self):
        hashmap = AdtHashMap(1, 1)
        self.assertFalse(hashmap.tableRetrieve(0))

    def testDeleteEmpty(self):
        hashmap = AdtHashMap(1, 1)
        self.assertFalse(hashmap.tableDelete(5))