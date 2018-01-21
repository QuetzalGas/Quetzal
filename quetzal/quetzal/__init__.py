from .datastructures import *

from .date import Date
from .datetime import DateTime
from .product import *
from .stock import Stock
from .user import User, UserContainer
from .employeepresent import EmployeePresent
from .employee import Employee
from .chocolatemilk import ChocolateMilk
from .order import Order

import inspect

class Quetzal:
    """
    +init()
    Initialiseer de winkel.

    Preconditie: geen.
    Postconditie: een lege winkel (zonder stock, gebruikers, of werknemers) is
    aangemaakt.
    """

    def __init__(self):
        self.now = 1
        self.started = False
        self.stock = Stock('dll')
        self.users = UserContainer('bs')
        self.employees = EmployeePresent()
        self.last_employee_id = 1
        self.history = []
        self.employee_ids = []

    """
    +add_to_stock(in item: Ingredient, in count = 1: integer)
    Voeg een ingredient toe aan de stock.

    Postconditie: het object zal toegevoegd worden aan de stock.
    """

    def add_to_stock(self, item):
        self.stock.add_item(item)

    """
    +add_user(in user: Gebruiker)
    Voeg een gebruiker `user` toe aan de winkel.

    Preconditie: de simulatie mag niet gestart zijn.
    Postconditie: een nieuwe gebruiker is toegevoegd.
    """

    def add_user(self, first_name, last_name, email):
        self.users.add_if_unknown_user(first_name, last_name, email)

    """
    +add_employee(in employee: Werknemer)
    Voeg een werknemer `employee` toe aan de winkel.

    Preconditie: de simulatie mag niet gestart zijn.
    Postconditie: een nieuwe werknemer is toegevoegd. Deze werknemer mag niet
    in een andere winkel worden toegevoegd.
    """

    def add_employee(self, first_name, last_name, workload):
        employee = Employee(
            self.last_employee_id,
            first_name,
            last_name,
            workload)
        self.employee_ids.append(self.last_employee_id)
        self.last_employee_id += 1
        self.employees.add_employee(employee)

    """
    +start_system()
    Start de simulatie logica. Nadat de simulatie draait zal het systeem een
    aantal veronderstellingen maken in verband met het aantal werknemers. Alle
    methoden die deze veronderstellingen breken zullen dit aangeduid hebben in
    hun precondities, en mogen dus niet meer gebruikt worden.

    Preconditie: de simulatie mag niet gestart zijn.
    Postconditie: de simulatie is gestart. De huidige tijdstap zal nul zijn.
    """

    def start_system(self):
        if self.started:
            raise RuntimeError(
                "Quetzal precondition broken: the simulation mustn't be running.")

        self.started = True
        self.timestep = 0
        self.new_orders = []
        self.order_queue = AdtQueue()

    """
    +is_started(): bool {query}
    Geeft terug of de simulatie gestart is.

    Preconditie: geen.
    Postconditie: geeft True als de simulatie gestart is, of anders False.
    """

    def is_started(self):
        return self.started

    """
    +place_order(in order: Bestelling, in datetime: DateTime)
    Plaats een bestelling `order` op tijdstip `datetime`.

    Preconditie: de simulatie moet gestart zijn. `datetime` mag niet in het
    verleden liggen.
    Postconditie: de bestelling is toegevoegd aan de simulatie logica.
    """

    def place_order(self, email, products, datetime):
        if not self.is_started():
            raise RuntimeError("Must be started")

        cm = ChocolateMilk(4)

        for i in products:
            k = self.stock.pop_item(i, datetime.get_date())[0]
            cm.add_product(k)

        order = Order(email, datetime, cm)

        self.new_orders.append(order)

    """
    +run_until(in datetime: DateTime)
    Loop de simulatie tot het tijdstip `datetime`.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: de simulatie zal stappen nemen totdat `datetime` is bereikt.
    Dit heeft dus ook alle postcondities van de `step` methode.
    """

    def run_until(self, timestep):
        # What if datetime < self.now? We get an infinite loop.
        while self.timestep < timestep:
            self.step()

    def get_state(self):
        state = []
        state.append(self.timestep)

        stack_string = "|"
        for i in self.employees.make_data_lists():
            stack_string += str(i.get_workload())
            stack_string += " "
        state.append(stack_string)  # stack

        for i in self.employee_ids:
            state.append(str(self.employees.get_remaining_workload(i)))

        new_orders_string = ''
        first = False

        for i in self.new_orders:
            i = i.get_chocolatemilk().get_workload()
            if not first:
                first = True
            else:
                new_orders_string += ','

            new_orders_string += format(i)

        state.append(new_orders_string)

        waiting_orders = ''
        first2 = False
        waiting = self.employees.get_waiting_orders()
        if waiting is not None:
            for i in waiting:
                i = i.get_chocolatemilk().get_workload()
                if not first2:
                    first2 = True
                else:
                    waiting_orders += ','

                waiting_orders += format(i)
        state.append(waiting_orders)

        state.append(self.stock.get_size('wit'))
        state.append(self.stock.get_size('melk'))
        state.append(self.stock.get_size('bruin'))
        state.append(self.stock.get_size('zwart'))
        state.append(self.stock.get_size('honing'))
        state.append(self.stock.get_size('marshmallow'))
        state.append(self.stock.get_size('chilipeper'))

        return state

    """
    +step()
    Neem een stap in de simulatie.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: zoveel mogelijk bestellingen worden verwerkt door de
    werknemers. Alle relevante informatie zal opgeslagen zijn om een logboek
    te presenteren.
    """

    def step(self):
        for i in self.new_orders:
            self.order_queue.enqueue(i)

        self.order_queue = self.employees.start(self.order_queue)[0]
        state = self.get_state()
        self.history.append(state)
        self.timestep += 1

        self.new_orders = []
        return state

    """
    +get_datetime(): DateTime {query}
    Geeft de huidige tijdstap van de simulatie.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: de huidige tijdstap van de simulatie wordt teruggegeven.
    """

    def get_datetime(self):
        pass

    """
    +log()
    Exporteer alle relevante informatie voor de toestand van de winkel in een
    menselijk leesbare html bestand.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: een logboek in het formaat "logx.html" zal geschreven worden,
    met x de tijdstap van de simulatie op het huidig moment.
    """

    def log(self):
        html = "<html>\n\
	<head>\n\
	<style>\n\
		table {border-collapse: collapse;}\n\
		table, td, th {border: 1px solid black;}\n\
	</style>\n\
</head>\n\
	<body>\n\
		<h1>Log</h1>\n\
		<table>\n\
			<thead>\n\
				<td>tijdstip</td>\n\
				<td>Stack</td>\n"
        employee_names = []

        for i in self.employee_ids:
            employee_names.append(self.employees.get_employee_name(i))

        for i in employee_names:
            html += "				<td>{}</td>\n".format(i)

        html += "				<td>Nieuwe bestellingen</td>\n\
				<td>Wachtende bestellingen</td>\n"

        stock = [
            "wit",
            "melk",
            "bruin",
            "zwart",
            "honing",
            "marshmallow",
            "chili"]

        for i in stock:
            html += "				<td>{}</td>\n".format(i)

        html += "			</thead>\n\
			<tbody>\n"

        self.step()

        for i in self.history:
            html += "				<tr>\n"

            for j in i:
                html += "					<td>{}</td>\n".format(j)

            html += "				</tr>\n"
        html += "			</tbody>\n\
		</table>\n\
	</body>\n\
</html>"

        with open('log{}.html'.format(self.timestep - 1), 'w') as f:
            f.write(html)
