#! /bin/python

import unittest
import tests

def test_adts():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    for test in tests.test_list:
        suite.addTest(unittest.makeSuite(test))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

test_adts()
