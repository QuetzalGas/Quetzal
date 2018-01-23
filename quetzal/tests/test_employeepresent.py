from quetzal import *
from unittest import TestCase


class TestEmployeePresent(TestCase):
    def testAddEmployee(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        self.assertEqual(present.stack.peek(), employee2)
        present.stack.delete()
        self.assertEqual(present.stack.peek(), employee1)

    def testAssignOrder(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        present._assign_order(order)
        self.assertEqual(present.stack.peek(), employee1)
        present._assign_order(order)
        self.assertEqual(employee1.order_handeling, order)
        self.assertEqual(employee1.credits_still_to_do, 5)
        self.assertEqual(employee2.order_handeling, order)
        self.assertEqual(employee2.credits_still_to_do, 5)

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
        present._assign_order(order1)
        present._assign_order(order2)
        present._process_and_done()
        self.assertIsNone(employee1.order_handeling)
        self.assertEqual(employee1.credits_still_to_do, 0)
        self.assertEqual(employee2.order_handeling, order1)
        self.assertEqual(employee2.credits_still_to_do, 2)
        self.assertEqual(present.handled_orders[0], order2)
        self.assertEqual(present.stack.peek(), employee1)
        self.assertEqual(present.employees_working[0], employee2)

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
        queue2 = AdtQueue()
        orders = present.start(queue)
        orders = present.start(queue2)
        self.assertIsNone(employee1.order_handeling)
        self.assertEqual(employee1.credits_still_to_do, 0)
        self.assertEqual(employee2.order_handeling, order1)
        self.assertEqual(employee2.credits_still_to_do, 2)
        self.assertEqual(orders[1][0], order2)
        self.assertFalse(present.stack.is_empty())

    def testStart2(self):
        present = EmployeePresent()
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        queue = AdtQueue()
        queue.enqueue(order1)
        orders = present.start(queue)
        order = orders[0].dequeue()
        self.assertEqual(order, order1)
        self.assertEqual(len(orders[1]), 0)

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
        present._assign_order(order1)
        present._assign_order(order2)
        present._process_and_done()
        list1 = [employee1]
        lists = present.make_data_lists()
        self.assertEqual(list1, lists)

    def testRemainingWorkload(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        present._assign_order(order1)
        present._assign_order(order2)
        present._process_and_done()
        self.assertEqual(present.get_remaining_workload(2), 2)
        self.assertIsNone(present.get_remaining_workload(5))

    def testGetEmployeeName(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        present._assign_order(order1)
        present._assign_order(order2)
        present._process_and_done()
        naam = "testvoornaam1 testachternaam1"
        self.assertEqual(present.get_employee_name(1), naam)
        self.assertIsNone(present.get_employee_name(3))

    def testGetWaitingOrders(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.add_employee(employee1)
        present.add_employee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order1 = Order(1, "time", choco)
        order2 = Order(2, "time", choco)
        order3 = Order(3, "time", choco)
        queue = AdtQueue()
        queue.enqueue(order1)
        queue.enqueue(order2)
        queue.enqueue(order3)
        present.start(queue)
        self.assertEqual(present.get_waiting_orders()[0], order3)
        self.assertIsNone(present.get_waiting_orders())