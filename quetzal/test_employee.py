from.employee import Employee
from.order import Order
from.chocolatemilk import ChocolateMilk
from unittest import TestCase

class TestEmployee(TestCase):
    def testInitAndGetters(self):
        employee = Employee(1, "testvoornaam1", "testachternaam1", 10)
        self.assertEqual(employee.get_id(), 1)
        self.assertEqual(employee.get_name(), "testvoornaam1 testachternaam1")
        self.assertEqual(employee.get_workload(), 10)

    def testSetLoad(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee1.set_load(15)
        self.assertEqual(employee1.get_workload(), 15)

    def testSetOrderLoad(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee1.set_orderLoad(order)
        self.assertEqual(employee1.orderHandeling, order)
        self.assertEqual(employee1.creditsToHandle, 5)
        self.assertEqual(employee1.creditsStillToDo, 5)

    def testProcess(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee1.set_orderLoad(order)
        testorder = employee1.process()
        self.assertEqual(testorder, order)
        self.assertIsNone(employee1.orderHandeling)
        self.assertEqual(employee1.creditsStillToDo, 0)
        self.assertEqual(employee1.creditsToHandle, 0)
        employee2 = Employee(1, "testvoornaam1", "testachternaam1", 3)
        employee2.set_orderLoad(order)
        testorder2 = employee2.process()
        self.assertIsNone(testorder2)
        self.assertEqual(employee2.orderHandeling, order)
        self.assertEqual(employee2.creditsStillToDo, 2)
        self.assertEqual(employee2.creditsToHandle, 5)
        testorder3 = employee2.process()
        self.assertEqual(testorder3, order)
        self.assertIsNone(employee2.orderHandeling)
        self.assertEqual(employee2.creditsToHandle, 0)
        self.assertEqual(employee2.creditsStillToDo, 0)