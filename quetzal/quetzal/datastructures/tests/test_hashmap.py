from quetzal import *
from unittest import TestCase


class TestHashmap(TestCase):
    # General

    def testRetrieveEmpty(self):
        hashmap = AdtHashMap(1, 1)
        try:
            test = hashmap[0]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    def testDeleteEmpty(self):
        hashmap = AdtHashMap(1, 1)
        try:
            del hashmap[0]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    # Tests for linear probing

    def testLinearProbing(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[3] = "test"
        hashmap[33] = "test2"
        self.assertEqual(hashmap.lijst[3].search_key, 3)
        self.assertEqual(hashmap.lijst[4].search_key, 33)
        hashmap["searchkey"] = "test3"
        self.assertEqual(hashmap.lijst[0].search_key, "searchkey")

    def testLinearProbingFull(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[3] = "test1"
        hashmap[33] = "test2"
        hashmap[23] = "test3"
        hashmap[88] = "test4"
        hashmap[123] = "test5"
        try:
            hashmap[13] = "test6"
            self.assertTrue(False)
        except MemoryError:
            self.assertTrue(True)

    def testGetLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[4] = "test"
        self.assertEqual(hashmap[4], "test")
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    def testDeleteLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[5] = "test"
        del hashmap[5]
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)
        self.assertTrue(hashmap.is_empty())

    def testContainsLP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[3] = "test1"
        hashmap[33] = "test2"
        hashmap[23] = "test3"
        self.assertTrue(3 in hashmap)
        self.assertTrue(33 in hashmap)
        self.assertTrue(23 in hashmap)
        self.assertFalse(56 in hashmap)

    # Tests for quadratic probing

    def testQuadraticProbing(self):
        hashmap = AdtHashMap(5, 1)
        hashmap[15] = "test"
        hashmap[25] = "test"
        hashmap[35] = "test"
        self.assertEqual(hashmap.lijst[0].search_key, 15)
        self.assertEqual(hashmap.lijst[1].search_key, 25)
        self.assertEqual(hashmap.lijst[4].search_key, 35)

    def testQuadraticProbingFull(self):
        hashmap = AdtHashMap(5, 1)
        hashmap[2] = "test"
        hashmap[7] = "test"
        hashmap[5] = "test"
        hashmap[15] = "test"
        hashmap[25] = "test"
        try:
            hashmap[35] = "test"
            self.assertTrue(False)
        except MemoryError:
            self.assertTrue(True)

    def testGetQP(self):
        hashmap = AdtHashMap(5, 1)
        hashmap[4] = "test"
        self.assertEqual(hashmap[4], "test")
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    def testDeleteQP(self):
        hashmap = AdtHashMap(5, 1)
        hashmap[5] = "test"
        del hashmap[5]
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)
        self.assertTrue(hashmap.is_empty())

    def testContainsQP(self):
        hashmap = AdtHashMap(5, 0)
        hashmap[3] = "test1"
        hashmap[33] = "test2"
        hashmap[23] = "test3"
        self.assertTrue(3 in hashmap)
        self.assertTrue(33 in hashmap)
        self.assertTrue(23 in hashmap)
        self.assertFalse(56 in hashmap)

    # Tests for separate chaining

    def testSeparateChaining(self):
        hashmap = AdtHashMap(5, 2)
        hashmap[15] = "test"
        hashmap[25] = "test"
        #self.assertEqual(hashmap.lijst[0].)

    def testSeparateChainingFull(self):
        hashmap = AdtHashMap(5, 2)
        hashmap[0] = "test"
        hashmap[1] = "test"
        hashmap[2] = "test"
        hashmap[3] = "test"
        hashmap[4] = "test"
        hashmap[5] = "test"
        hashmap[6] = "test"
        self.assertTrue(True)

    def testGetSC(self):
        hashmap = AdtHashMap(5, 2)
        hashmap[4] = "test"
        self.assertEqual(hashmap[4], "test")
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    def testDeleteSC(self):
        hashmap = AdtHashMap(5, 1)
        hashmap[5] = "test"
        del hashmap[5]
        try:
            test = hashmap[5]
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)
        self.assertTrue(hashmap.is_empty())
        hashmap[5] = "test"
        hashmap[15] = "test"
        hashmap[25] = "test"
        del hashmap[15]
        self.assertEqual(hashmap.lijst[0].get_length(), 2)
        del hashmap[5]
        del hashmap[25]
        self.assertTrue(hashmap.is_empty())