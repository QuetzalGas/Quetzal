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
        present.addEmployee(employee1)
        present.addEmployee(employee2)
        self.assertEqual(present.stack.getTop(), employee2)
        present.stack.pop()
        self.assertEqual(present.stack.getTop(), employee1)

    def testProcessAndDone_AndSetOrder(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.addEmployee(employee1)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        employee2.set_orderLoad(order)
        self.assertEqual(employee2.orderHandeling, order)
        self.assertEqual(employee2.creditsStillToDo, 5)
        self.assertEqual(employee2.creditsToHandle, 5)
        present.employeesPresent.insertEnd(employee2)


    def testAssignOrder(self):
        employee1 = Employee(1, "testvoornaam1", "testachternaam1", 10)
        employee2 = Employee(2, "testvoornaam2", "testachternaam2", 3)
        present = EmployeePresent()
        present.addEmployee(employee1)
        present.addEmployee(employee2)
        choco = ChocolateMilk(1)
        choco.workload = 5
        order = Order(1, "time", choco)
        present.assignOrder(order)

    def testStart(self):
        pass