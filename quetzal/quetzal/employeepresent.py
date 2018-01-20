from .datastructures import *
from .employee import Employee


class EmployeePresent:
    def __init__(self):
        """ Initialises a new  order handling system.

        PRE: None
        POST: A new system is initialised.
        """
        self.employees_working = []
        self.stack = AdtStack()
        self.handled_orders = []
        self.employees_present = []
        self.order_queue = None

    def __del__(self):
        """ Deletes the system.

        PRE: None
        POST: The object will be destroyed.
        """
        self.stack.destroy_stack()

    def add_employee(self, employee):
        """ Registers an employee for the work day.

        :param employee: The employee that starts to work

        PRE: Employee has to be of the employee class.
        POST: Employee will be on the stack and available to handle orders.
        """
        self.stack.push(employee)
        self.employees_present.append(employee)

    def start(self, queue):
        """ Begin processing the queue with orders.

        :param queue: The queue with the active orders.
        :return: None if no employee is available or a list with orders that were handled.

        PRE: Queue has to contain valid orders (from order class) that are not yet processed.
        POST: The first order will get processed if there are employees available.
        """
        self.order_queue = queue
        reserve = AdtQueue()
        reserve2 = AdtQueue()
        self.handled_orders = []
        self._process_and_done()
        while not queue.is_empty():
            order = self.order_queue.dequeue()
            if not self.stack.is_empty():
                self._assign_order(order)
            else:
                reserve.enqueue(order)
                reserve2.enqueue(order)
        self.order_queue = reserve2
        return reserve, self.handled_orders

    def _assign_order(self, order):
        """ Assigns an order to one of the employees.

        :param order: The order that's going to be assigned to an employee.

        PRE: None
        POST: The employee that was added last on the stack now has an order to process.
        """
        employee_node = self.stack.pop_and_return()[0]
        employee = employee_node.item
        employee.set_order_load(order)
        self.employees_working.append(employee)

    def _process_and_done(self):
        """ Processes the orders and checks which employees are done.

        PRE: None
        POST: Every order gets processed for one timestep and employees that are finished are back on the stack.
        """
        index_to_delete = []
        for j in range(0, len(self.employees_working)):
            i = self.employees_working[j]
            order = i.get_order()
            i.process()
            if i.get_credits_still_to_do() == 0:
                self.stack.push(i)
                self.handled_orders.append(order)
                index_to_delete.append(j)
        index_to_delete.reverse()
        for index in index_to_delete:
            del self.employees_working[index]

    def make_data_lists(self):
        """ Makes a list with all the employees on the stack.

        :return: A list with all the employees on the stack.

        PRE: None
        POST: Stack_list has a list with all the employees that are not working.
        """
        stack_list = []
        while not self.stack.is_empty():
            employee_node = self.stack.pop_and_return()[0]
            employee = employee_node.item
            stack_list.append(employee)
        stack_list.reverse()
        for i in stack_list:
            self.stack.push(i)
        return stack_list

    def get_remaining_workload(self, id_):
        """ Searches for the remaining workload of an employee.

        :param id_: The id of the employee to search.
        :return: None if the employee is not working, else the credits still to do.

        PRE: id_ has to be a valid employee id.
        POST: Credits contains the workload of the employee with the given id or None if the id doesn't match.
        """
        credits = None
        for i in self.employees_present:
            if id_ == i.get_id():
                credits = i.get_credits_still_to_do()
                break
        return credits

    def get_employee_name(self, id_):
        """ Searches for the name of an employee.

        :param id_: The id of the employee to find.
        :return: The name of the found employee or None if he doesn't exist.

        PRE: id_ has to be a valid employee id.
        POST: Name will be the full name of the employee if an employee with that id exists. Otherwise it will be None.
        """
        name = None
        for i in self.employees_present:
            if id_ == i.get_id():
                name = i.get_name()
                break
        return name

    def get_waiting_orders(self):
        """ Makes a list with all the orders that are still waiting to be processed.

        :return: A list with the contents the queue.

        PRE: None
        POST: Queuelist will contain either None if the queue is empty or a list with all the orders that are waiting to be processed.
        """
        if self.order_queue is None or self.order_queue.is_empty():
            return None
        else:
            queuelist = []
            while not self.order_queue.is_empty():
                order = self.order_queue.dequeue()

                queuelist.append(order)
            return queuelist
