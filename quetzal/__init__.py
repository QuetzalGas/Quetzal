from .date import Date
from .datetime import DateTime

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

    """
    +add_to_stock(in item: Ingredient, in count = 1: integer)
    Voeg een ingredient toe aan de stock.

    Preconditie: count moet strikt groter dan nul zijn.
    Postconditie: het object zal toegevoegd worden aan de stock.
    """
    def add_to_stock(self, item, count=1):
        if item == Honey:
            print('werkt')

    """
    +add_user(in user: Gebruiker)
    Voeg een gebruiker `user` toe aan de winkel.

    Preconditie: de simulatie mag niet gestart zijn.
    Postconditie: een nieuwe gebruiker is toegevoegd.
    """
    def add_user(self, user):
        pass

    """
    +add_employee(in employee: Werknemer)
    Voeg een werknemer `employee` toe aan de winkel.

    Preconditie: de simulatie mag niet gestart zijn.
    Postconditie: een nieuwe werknemer is toegevoegd. Deze werknemer mag niet
    in een andere winkel worden toegevoegd.
    """
    def add_employee(self, employee):
        pass

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
            raise RuntimeError("Quetzal precondition broken: the simulation mustn't be running.")

        self.started = True

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
    def place_order(self, order, datetime):
        pass

    """
    +run_until(in datetime: DateTime)
    Loop de simulatie tot het tijdstip `datetime`.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: de simulatie zal stappen nemen totdat `datetime` is bereikt.
    Dit heeft dus ook alle postcondities van de `step` methode.
    """
    def run_until(self, datetime):
        # What if datetime < self.now? We get an infinite loop.
        while self.now < datetime.time:
            self.step()

    """ 
    +step()
    Neem een stap in de simulatie.

    Preconditie: de simulatie moet gestart zijn.
    Postconditie: zoveel mogelijk bestellingen worden verwerkt door de
    werknemers. Alle relevante informatie zal opgeslagen zijn om een logboek
    te presenteren.
    """
    def step(self):
        pass

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
        employees = ["Wim Hofkens", "Jane Doe"]

        for i in employees:
            html += "				<td>{}</td>\n".format(i)

        html += "				<td>Nieuwe bestellingen</td>\n\
				<td>Wachtende bestellingen</td>\n"

        stock = ["wit", "melk", "bruin", "zwart", "honing", "marshmallow", "chili"]

        for i in stock:
            html += "				<td>{}</td>\n".format(i)

        html += "			</thead>\n\
			<tbody>\n"

        html += "			</tbody>\n\
		</table>\n\
	</body>\n\
</html>"

        with open('test-html.html', 'w') as f:
            f.write(html)
