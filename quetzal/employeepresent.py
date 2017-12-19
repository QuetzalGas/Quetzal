from .datastructures import *
from .employee import Employee

class EmployeePresent:
    def __init__(self):
        self.employeesPresent = adt_doubly_linked_list.AdtDoublyLinkedList()
        self.stack = adt_stack.AdtStack()
        self.queue = None
        self.handeledOrders = []
        self.stackList = []

    def __del__(self):
        self.stack.destroyStack()

    def add_employee(self, employee):
        """
        Adds an employee to the worklist.
        :param employee: The employee that starts to work
        :return: True if it succeeded. False otherwise.
        PRE: Employee has to be of the employee class.
        POST: Employee will be on the stack and available to handle orders.
        """
        self.stack.push(employee)
        return True

    def start(self, queue):
        """
        Begin processing the queue with orders.
        :param queue: The queue with the active orders.
        :return: None if no employee is available or a list with orders that were handeled.
        PRE: Queue has to contain valid orders (from order class) that are not yet processed.
        POST: The first order will get processed if there are employees available.
        """
        #Reset handeledOrders
        self.handeledOrders = []
        self.queue = queue
        order = self.queue.dequeue()
        if self.stack.isEmpty():
            #Resume the rest of the orders
            self.processAndDone()
            return None
        else:
            self.assignOrder(order)
            return self.handeledOrders

    def assignOrder(self, order):
        """
        Assigns an order to one of the employees.
        :param order: The order that's going to be assigned to an employee
        """
        employee = self.stack.popAndReturn()[0]
        employee.set_orderLoad(order)
        self.employeesPresent.insertEnd(employee)
        self.processAndDone()

    def processAndDone(self):
        """
        Processes the orders and checks which employees are done.
        """
        for i in self.employeesPresent:
            order = i.item.process()
            if order is not None:
                self.handeledOrders = order
            if i.item.creditsStillToDo == 0:
                self.stack.push(i.item)

    def printStack(self):
        """
        Makes a list with all the workload of all the employees on the stack.
        :return: A list with all the workloads.
        """
        while not self.stack.isEmpty():
            employee = self.stack.popAndReturn()[0].item
            self.stackList.append(employee.get_workload())
        for i in self.stackList:
            self.stack.push(i)
        return self.stackList.reverse()
