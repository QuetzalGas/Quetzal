from.datastructures import *
from.employee import Employee

class EmployeePresent:
    def __init__(self):
        self.employeesWorking = [] #TODO double linked list can be used
        self.stack = adt_stack.AdtStack()
        self.queue = None
        self.handeledOrders = []
        self.employeesPresent = []

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
        self.employeesPresent.append(employee)
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
        if self.stack.isEmpty() or queue.isEmpty():
            #Resume the rest of the order
            self.processAndDone()
            return None
        else:
            while not self.stack.isEmpty() and not queue.isEmpty():
                order = self.queue.dequeue()
                self.assignOrder(order)
            self.processAndDone()
        return self.handeledOrders

    def assignOrder(self, order):
        """
        Assigns an order to one of the employees.
        :param order: The order that's going to be assigned to an employee
        """
        employee = self.stack.popAndReturn()[0]
        employee = employee.item
        employee.set_orderLoad(order)
        self.employeesWorking.append(employee)

    def processAndDone(self):
        """
        Processes the orders and checks which employees are done.
        """
        for i in self.employeesWorking:
            order = i.process()
            if order is not None:
                self.handeledOrders.append(order)
                self.stack.push(i)
                self.employeesWorking.remove(i)

    def makeDataLists(self):
        """
        Makes a list with all the workload of all the employees on the stack.
        :return: A list with all the workloads.
        """
        self.stackList = []
        self.employeesWorkingList = []

        while not self.stack.isEmpty():
            employee = self.stack.popAndReturn()[0]
            employee = employee.item
            self.stackList.append(employee.get_workload())
        for i in self.stackList:
            self.stack.push(i)
        self.stackList.reverse()

        for i in self.employeesWorking:
            self.employeesWorkingList.append((i, i.get_credits_still_to_do()))

        return self.stackList, self.employeesWorkingList

    def get_remaining_workload(self, id_):
        """
        Searches for the remaining workload of an employee.
        :param id_: The id of the employee to search.
        :return: None if the employee is not working, else the credits still to do.
        """
        for i in self.employeesPresent:
            if id_ == i.get_id:
                return i.get_credits_still_to_do()
            else:
                return None

    def get_employee_name(self, id_):
        """
        Searches for the name of an employee.
        :param id_: The id of the employee to find.
        :return: The name of the found employee or None if he doesn't exist.
        """
        for i in self.employeesPresent:
            if id_ == i.get_id:
                return i.get_name()
            else:
                return None