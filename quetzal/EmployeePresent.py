from.datastructures import *

class employee_present:
    def __init__(self):
        self.employeesPresent = adt_doubly_linked_list.AdtDoublyLinkedList()
        self.stack = adt_stack.AdtStack()
        self.queue = None
        self.handeledOrders = []

    def __del__(self):
        self.stack.destroyStack()

    def addEmployee(self, employee):
        """
        Adds an employee to the worklist.
        :param employee: The employee that starts to work
        :return: True if it succeeded. False otherwise.
        """
        self.stack.push(employee)
        return True

    def start(self, queue):
        """

        :param queue:
        :return:
        """
        #Reset handeledOrders
        self.handeledOrders = []
        self.queue = queue
        order = self.queue.dequeue()
        if self.stack.isEmpty():
            return None
        else:
            self.assignOrder(order)
            return self.handeledOrders

    def assignOrder(self, order):
        """
        Assigns an order to one of the employees.
        :param order:
        :return:
        """
        employee = self.stack.popAndReturn()[0]
        employee.set_orderLoad(order)
        self.employeesPresent.insertEnd(employee)
        self.processAndDone()

    def processAndDone(self):
        """

        :return:
        """
        for i in self.employeesPresent:
            order = i.item.process()
            if order is not None:
                self.handeledOrders = order
            if i.item.creditsStillToDo == 0:
                self.stack.push(i.item)

