class Employee:
    def __init__(self, id_, first_name, last_name, workload):
        """ Initialises a new employee.

        :param id_: The id of the employee.
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
        self.credits_still_to_do = ""
        self.credits_to_handle = 0
        self.order_handeling = None

    def __del__(self):
        """ Deletes an employee.

        :return: True if the employee was deleted. False if not.

        PRE: None
        POST: The employee will not exist anymore.
        """
        self.id = None
        self.firstName = None
        self.lastName = None
        self.workload = 0
        self.credits_still_to_do = 0
        self.credits_to_handle = 0
        if self.order_handeling is not None:
            return False
        self.order_handeling = None
        return True

    def get_id(self):
        """ Returns the employee's id.

        :return: The id of the employee.

        PRE: None
        POST: Id will be the id of the employee.
        """
        return self.id

    def get_name(self):
        """ Returns the employee's name.

        :return: The name of the employee.

        PRE: None
        POST: Name will be a string with both first and last name.

        """
        return self.firstName + " " + self.lastName

    def get_workload(self):
        """ Returns the workload of the employee.

        :return: The workload of this employee.

        PRE: None
        POST: Workload will be the workload of the employee.
        """
        return self.workload

    def get_credits_still_to_do(self):
        """ Returns the credits the employee still has to process.

        :return: The remaining credits of an order.

        PRE: None
        POST: Credits will be the credits the employee still has to handle.
        """
        return self.credits_still_to_do

    def get_order(self):
        """ Returns the order the employee is working on.

        :return: The order the employee is working on.

        PRE:None
        POST: Order handling will be the order that the employee is working on.
        """
        return self.order_handeling

    def set_load(self, load):
        """ Sets the workload of the employee to a new value.

        :param load: The new workload.

        PRE: Workload has to be a valid number.
        POST: The employee has a new workload.
        """
        self.workload = load

    def set_order_load(self, order):
        """ Sets the order that the employee has to process.

        :param order: The order to process.

        PRE: Order has to be from the Order class and it has to have valid data. Order_handeling has to be empty.
        POST: The employee now has the data to process an order.
        """
        self.order_handeling = order
        self.credits_to_handle = order.get_chocolatemilk().get_workload()
        self.credits_still_to_do = self.credits_to_handle

    def process(self):
        """ Handles an order with a certain workload.

        PRE: None
        POST: The order will partially or fully be processed.
        """
        self.credits_still_to_do = self.workload - self.credits_still_to_do
        if self.credits_still_to_do < 0:
            self.credits_still_to_do = -self.credits_still_to_do
            return None
        else:
            order = self.order_handeling
            self.credits_still_to_do = ""
            self.credits_to_handle = 0
            self.order_handeling = None
            return order
