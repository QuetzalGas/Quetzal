from.datastructures import *
from.employee import Employee


class EmployeePresent:
    def __init__(self):
        self.employees_working = []  # TODO double linked list can be used
        self.stack = AdtStack()
        self.handeled_orders = []
        self.employees_present = []
        self.order_queue = None

    def __del__(self):
        self.stack.destroy_stack()

    def add_employee(self, employee):
        """
        Adds an employee to the worklist.
        :param employee: The employee that starts to work
        :return: True if it succeeded. False otherwise.
        PRE: Employee has to be of the employee class.
        POST: Employee will be on the stack and available to handle orders.
        """
        self.stack.push(employee)
        self.employees_present.append(employee)
        return True

    def start(self, queue):
        """
        Begin processing the queue with orders.
        :param queue: The queue with the active orders.
        :return: None if no employee is available or a list with orders that were handeled.
        PRE: Queue has to contain valid orders (from order class) that are not yet processed.
        POST: The first order will get processed if there are employees available.
        """
        # Reset handeled_orders
        self.handeled_orders = []
        self.order_queue = queue
        if self.stack.is_empty() or queue.is_empty():
            # Resume the rest of the order
            self.process_and_done()
            return None
        else:
            while not self.stack.is_empty() and not queue.is_empty():
                order = self.order_queue.dequeue()
                self.assign_order(order)
            self.process_and_done()
        return self.handeled_orders

    def assign_order(self, order):
        """
        Assigns an order to one of the employees.
        :param order: The order that's going to be assigned to an employee
        """
        employee_node = self.stack.pop_and_return()[0]
        employee = employee_node.item
        employee.set_order_load(order)
        self.employees_working.append(employee)

    def process_and_done(self):
        """
        Processes the orders and checks which employees are done.
        """
        for i in self.employees_working:
            if i.get_credits_still_to_do == "":
                # self.handeled_orders.append(order)
                self.stack.push(i)
                self.employees_working.remove(i)
            i.process()

    def make_data_lists(self):
        """
        Makes a list with all the workload of all the employees on the stack.
        :return: A list with all the workloads.
        """
        self.stack_list = []
        self.employees_working_list = []

        while not self.stack.is_empty():
            employee_node = self.stack.pop_and_return()[0]
            employee = employee_node.item
            self.stack_list.append(employee)
        self.stack_list.reverse()
        for i in self.stack_list:
            self.stack.push(i)

        return self.stack_list

    def get_remaining_workload(self, id_):
        """
        Searches for the remaining workload of an employee.
        :param id_: The id of the employee to search.
        :return: None if the employee is not working, else the credits still to do.
        """
        credits = None
        for i in self.employees_present:
            if id_ == i.get_id():
                credits = i.get_credits_still_to_do()
                break
        return credits

    def get_employee_name(self, id_):
        """
        Searches for the name of an employee.
        :param id_: The id of the employee to find.
        :return: The name of the found employee or None if he doesn't exist.
        """
        name = None
        for i in self.employees_present:
            if id_ == i.get_id():
                name = i.get_name()
                break
        return name

    # def get_waiting_orders(self):
    #     if self.order_queue is None or self.order_queue.is_empty():
    #         return None
    #     else:
    #         queuelist = []
    #         keeporders = []
    #         while not self.order_queue.is_empty():
    #             order = self.order_queue.dequeue()
    #             keeporders.append(order)
    #             queuelist.append(order)
    #         return queuelist
