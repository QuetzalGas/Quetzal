from datastructures import *
from unittest import TestCase
from random import shuffle

class TestTwoThreeFourTree(TestCase):
    def test_init_and_delete(self):
        t = AdtTwoThreeFourTree()
        self.assertTrue(t.is_empty())
        self.assertEqual(t.root, None)
        t[0] = 45
        t[1] = 10
        self.assertFalse(t.is_empty())
        self.assertNotEqual(t.root, None)

    def test_insert(self):
        t = AdtTwoThreeFourTree()
        t[10] = "10a"
        t[10] = "10b"
        t[60] = "60"
        t[10] = "10c"
        self.assertFalse(t.is_empty())
        t[30] = "30"
        t[40] = "40"
        self.assertEqual(t.root.amount, 1)
        t[70] = "70"
        self.assertEqual(t.root.amount, 1)
        t[90] = "90"
        self.assertEqual(t.root.amount, 2)
        self.assertEqual(t.root.children[0].amount, 1)
        self.assertEqual(t.root.children[1].amount, 1)
        self.assertEqual(t.root.children[2].amount, 2)
        self.assertEqual(t.root.children[3], None)

    def test_insert_2(self):
        t = AdtTwoThreeFourTree()
        keys = [60, 30, 10, 20, 50, 40, 70, 80, 15, 90, 100]
        for k in keys:
            t[k] = k
        filename = "test2.dot"
        with open(filename, "w") as file:
            file.write(repr(t))
        for k in keys:
            self.assertTrue(k in t)

    def test_insert_and_delete(self):
        t = AdtTwoThreeFourTree()
        keys = [60, 30, 10, 20, 50, 40, 70, 80, 15, 90, 100]
        for k in keys:
            t[k] = k
        to_delete = keys[4:]
        for k in to_delete:
            del t[k]
            keys.remove(k)
            filename = "test2_" + str(k) + ".dot"
            with open(filename, "w") as file:
                file.write(repr(t))
        for k in keys:
            self.assertTrue(k in t)
        for k in to_delete:
            self.assertFalse(k in t)

    def test_delete(self):
        t = AdtTwoThreeFourTree()
        k1 = [10, 100, 30, 80, 50]
        k2 = [60, 70, 40]
        k3 = [90, 20]
        keys = [100, 50, 60, 40, 90, 20]
        for k in k1:
            t[k] = k
        del t[10]
        for k in k2:
            t[k] = k
        del t[80]
        for k in k3:
            t[k] = k
        del t[30]
        del t[70]
        for k in keys:
            self.assertTrue(k in t)
        for k in [10, 80, 30, 70, 4]:
            self.assertFalse(k in t)

    def test_duplicate(self):
        t = AdtTwoThreeFourTree()
        t[10] = "10a"
        t[10] = "10b"
        t[10] = "10c"
        t[30] = "30a"
        t[90] = "90a"
        t[90] = "90b"
        t[80] = "80a"
        self.assertEqual(t[10], "10a")
        del t[10]
        self.assertEqual(t[10], "10b")
        t[50] = "50a"
        del t[10]
        self.assertEqual(t[10], "10c")
        del t[10]
        self.assertFalse(10 in t)
        with self.assertRaises(KeyError):
            x = t[10]
        self.assertTrue(30 in t)
        self.assertTrue(90 in t)
        self.assertTrue(80 in t)
        self.assertTrue(50 in t)
        self.assertEqual(t[30], "30a")
        self.assertEqual(t[90], "90a")
        self.assertEqual(t[80], "80a")
        self.assertEqual(t[50], "50a")
        del t[90]
        self.assertEqual(t[90], "90b")
        del t[90]
        self.assertFalse(90 in t)
        with self.assertRaises(KeyError):
            x = t[90]
        del t[30]
        del t[80]
        del t[50]
        self.assertFalse(30 in t)
        self.assertFalse(80 in t)
        self.assertFalse(50 in t)
        with self.assertRaises(KeyError):
            x = t[30]
        with self.assertRaises(KeyError):
            x = t[80]
        with self.assertRaises(KeyError):
            x = t[50]
        self.assertTrue(t.is_empty())



    def test_mega_fuzz(self):
        rounds = 20
        unique_insertions = 10

        print()
        for k in range(1, rounds):
            print('Fuzz round', k)

            keys = [x for x in range(1, unique_insertions)]
            shuffle(keys)

            for i in range(0, 4):
                # Duplicate the last N elements for insertion
                duplicates = keys[-10:]
                keys.extend(duplicates)
                shuffle(keys)

            # Explicitly creates duplicates of a higher multiplicity.
            duplicates = keys[-3:]
            for i in range(0, 3):
                keys.extend(duplicates)
            shuffle(keys)
            tree = AdtTwoThreeFourTree()
            # Insert all keys.
            for i in keys:
                tree[i] = i

            # Check for validity.
            #inorder_list_of_keys = [x[0] for x in rb]
            #self.assertEqual(sorted(inorder_list_of_keys), inorder_list_of_keys)

            # Check if everything can be found.
            for i in keys:
                self.assertTrue(i in tree)

            copy_of_ = list(keys)
            original = list(keys)
            shuffle(keys)

            removed = []

            for i in keys:
                # if i == 3:
                #     filename = "fuz_234_" + str(k) + ".dot"
                #     with open(filename, "w") as file:
                #         file.write(repr(tree))
                del tree[i]
                original.remove(i)
                removed.append(i)

                #inorder_list_of_keys = [x[0] for x in rb]
                #self.assertEqual(sorted(inorder_list_of_keys), inorder_list_of_keys)

                # If it's still in the original, then it also must be in our tree.
                for j in original:
                    self.assertTrue(j in tree)

                for j in removed:
                    # Duplicates can be found multiple times.
                    if j in original:
                        self.assertTrue(j in tree)
                    else:
                        self.assertFalse(j in tree)
