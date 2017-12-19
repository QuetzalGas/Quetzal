class Employee:
    def __init__(self, id_, first_name, last_name, workload):
        """
        Initialises a new employee.
        :param id: The id of the employee.
        :param first_name: The first name of the empoyee.
        :param last_name: The last name of the employee.
        :param workload: The workload that the employee can handle.
        PRE: Workload has to be a valid number.
        POST: A new employee with name, id and workload exists.
        """
        self.id = id_
        self.firstName = first_name
        self.lastName = last_name
        self.workload = workload
        self.creditsStillToDo = 0
        self.creditsToHandle = 0
        self.orderHandeling = None
        #TODO add to datastructure for employees

    def __del__(self):
        """
        Deletes an employee.
        :return: True if the employee was deleted. False if not.
        POST: The employee will not exist anymore.
        """
        self.id = None
        self.firstName = None
        self.lastName = None
        self.workload = 0
        self.creditsStillToDo = 0
        self.creditsToHandle = 0
        self.orderHandeling = None
        #TODO remove from datastructure for employees
        return True

    def get_id(self):
        """
        Returns the employee's id.
        :return: The id of the employee.
        """
        return self.id

    def get_name(self):
        """
        Returns the employee's name.
        :return: The name of the employee.
        """
        return self.firstName + " " + self.lastName

    def get_workload(self):
        """
        Returns the workload of the employee.
        :return: The workload of this employee.
        """
        return self.workload

    def set_load(self, load):
        """
        Sets the workload of the employee to a new value.
        :param load: The new workload.
        PRE: Workload has to be a valid number.
        POST: The emloyee has a new workload.
        """
        self.workload = load

    def set_orderLoad(self, order):
        """
        Sets the order that the employee has to process.
        :param order: The order to process
        PRE: Order has to be from the Order class and it has to have valid data. Orderhandeling has to be empty.
        POST: The employee now has the data to process an order.
        """
        self.orderHandeling = order
        self.creditsToHandle = order.get_chocolatemilk().getWorkLoad()
        self.creditsStillToDo = self.creditsToHandle

    def process(self):
        """
        Handles an order with a certain workload.
        POST: The order will partially or fully be processed.
        """
        self.creditsStillToDo = self.workload - self.creditsStillToDo
        if self.creditsStillToDo < 0:
            self.creditsStillToDo = -self.creditsStillToDo
            return None
        else:
            order = self.orderHandeling
            self.creditsStillToDo = 0
            self.creditsToHandle = 0
            self.orderHandeling = None
            return order
