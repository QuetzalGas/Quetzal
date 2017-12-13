from Stack import Stack
import time

#Interval for checking orders (seconds)
CHECKTIMES = 30

class employee_present:
    def __init__(self):
        self.employeesPresent = None
        self.stack = Stack()

    def __del__(self):
        self.stack.destroyStack()
        #TODO destroy employeesPresent

    def addEmployee(self, employee):
        """
        Adds an employee to the worklist
        :param employee: The employee that starts to work
        :return: True if it succeeded. False otherwise.
        """
        #TODO add employee to employeesPresent
        self.stack.push(employee)
        employee.setWorkday(self)
        return True

    def assignOrder(self, order):
        """
        Assigns an order to one of the employees.
        :param order:
        :return:
        """
        while self.stack.isEmpty():
            time.sleep(CHECKTIMES)
        employee = self.stack.pop()[1]
        employee.process(order)
        return True

    def putBackOnStack(self, employee):
        self.stack.push(employee)


    def isOccupied(self):
        """

        :return:
        """
        pass
