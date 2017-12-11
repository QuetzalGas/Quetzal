from Stack import Stack

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
        return True

    def assignOrder(self, order):
        """
        Assigns an order to one of the employees.
        :param order:
        :return:
        """
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

    def checkCompleted(self):