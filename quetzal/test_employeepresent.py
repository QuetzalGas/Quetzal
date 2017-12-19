from.employeepresent import EmployeePresent
from.employee import Employee
from.order import Order
from.datastructures import adt_queue
from.chocolatemilk import ChocolateMilk
from unittest import TestCase

class TestEmployeePresent(TestCase):
    def testAddEmployee(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        self.assertEqual(present.stack.getTop(), employee2)
        present.stack.pop()
        self.assertEqual(present.stack.getTop(), employee1)

    def testAssignOrder(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        present.assignOrder(order)
        present.assignOrder(order)
        self.assertEqual(employee1.orderHandeling, order)
        self.assertEqual(employee1.creditsStillToDo, 5)
        self.assertEqual(employee1.creditsToHandle, 5)
        self.assertEqual(employee2.orderHandeling, order)
        self.assertEqual(employee2.creditsToHandle, 5)
        self.assertEqual(employee2.creditsStillToDo, 5)


    def testProcessAndDone(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        present.assignOrder(order1)
        present.assignOrder(order2)
        present.processAndDone()
        self.assertIsNone(employee1.orderHandeling)
        self.assertEqual(employee1.creditsStillToDo, 0)
        self.assertEqual(employee1.creditsToHandle, 0)
        self.assertEqual(employee2.orderHandeling, order1)
        self.assertEqual(employee2.creditsStillToDo, 2)
        self.assertEqual(present.handeledOrders[0], order2)
        self.assertFalse(present.stack.isEmpty())

    def testStart(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        queue = adt_queue.AdtQueue()
        queue.enqueue(order1)
        queue.enqueue(order2)
        orders = present.start(queue)
        self.assertIsNone(employee1.orderHandeling)
        self.assertEqual(employee1.creditsStillToDo, 0)
        self.assertEqual(employee1.creditsToHandle, 0)
        self.assertEqual(employee2.orderHandeling, order1)
        self.assertEqual(employee2.creditsStillToDo, 2)
        self.assertEqual(orders[0], order2)
        self.assertFalse(present.stack.isEmpty())

    def testMakeDataLists(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        present.assignOrder(order1)
        present.assignOrder(order2)
        present.processAndDone()
        list1 = [employee1.workload]
        list3 = [(employee2, 2)]
        lists = present.makeDataLists()
        self.assertEqual(list1, lists[0])
        self.assertEqual(list3, lists[1])