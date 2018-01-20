#! /bin/python

import unittest
import tests

def test_quetzal():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    for test in tests.test_list:
        suite.addTest(unittest.makeSuite(test))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

test_quetzal()
