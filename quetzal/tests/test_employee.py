from quetzal import *
from unittest import TestCase


class TestEmployee(TestCase):
    def testInitAndGetters(self):
        employee = Employee(1, "testvoornaam1", "testachternaam1", 10)
        self.assertEqual(employee.get_id(), 1)
        self.assertEqual(employee.get_name(), "testvoornaam1 testachternaam1")
        self.assertEqual(employee.get_workload(), 10)
        employee.credits_still_to_do = 5
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee.order_handeling = order
        self.assertEqual(employee.get_credits_still_to_do(), 5)
        self.assertEqual(employee.get_order(), order)

    def testSetLoad(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee1.set_load(15)
        self.assertEqual(employee1.get_workload(), 15)

    def testSetOrderLoad(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee1.set_order_load(order)
        self.assertEqual(employee1.order_handeling, order)
        self.assertEqual(employee1.credits_still_to_do, 5)

    def testProcess(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee1.set_order_load(order)
        testorder = employee1.process()
        self.assertEqual(testorder, order)
        self.assertIsNone(employee1.order_handeling)
        self.assertEqual(employee1.credits_still_to_do, 0)
        employee2 = Employee(1, "testvoornaam1", "testachternaam1", 3)
        employee2.set_order_load(order)
        testorder2 = employee2.process()
        self.assertIsNone(testorder2)
        self.assertEqual(employee2.order_handeling, order)
        self.assertEqual(employee2.credits_still_to_do, 2)
        testorder3 = employee2.process()
        self.assertEqual(testorder3, order)
        self.assertIsNone(employee2.order_handeling)
        self.assertEqual(employee2.credits_still_to_do, 0)
