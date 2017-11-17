from .date import Date
from .datetime import DateTime
from .honey import Honey
from .marshmallow import Marshmallow

import inspect

class Quetzal:
    def __init__(self):
        self.now = 1

    def add_to_stock(self, item, count=1):
        if item == Honey:
            print('werkt')

    def add_user(self, user):
        pass

    def add_employee(self, employee):
        pass

    def start_system(self):
        pass

    def place_order(self, order, datetime):
        pass

    def run_until(self, datetime):
        while self.now < datetime.time:
            self.step()

    def step(self):
        pass

    def log(self):
        pass
