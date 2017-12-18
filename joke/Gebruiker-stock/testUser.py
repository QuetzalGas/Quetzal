from unittest import TestCase
from gebruiker import UserContainer, User

"""
To test: change in the class testUserContainer the type (bs, 23, 234, (rb), h)
"""

class testUserContainer(TestCase):

    def testCheckUser(self, type='234'):
        container = UserContainer(type)
        container.checkUser(5, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(5, 'Morty', 'duwaerts', 'scared@gmail.com')
        container.checkUser(5, 'Ronan', 'Marvel', 'coolboy1452@uantwerpen.com')
        container.checkUser(5, 'Tina', 'Turner', 'power@gmail.com')
        container.checkUser(5, 'powerpuff', 'girl', 'pinklady@hotmail.com')
        container.checkUser(5, 'Rick', 'sanchez', 'getSchwifty@universe.com')
        container.checkUser(5, 'Arthur', 'Dent', 'still-flying@42life.com')
        container.checkUser(5, 'Time', 'Machine', 'time.machines@gmail.com')
        container.checkUser(28, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(12, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(5, 'octo', 'ananas', 'at@gmail.com')
        container.checkUser(5, 'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        container.checkUser(5, 'Witchking-of', 'Angmar', 'barad.dur@mordor.be')

    def testRetrieveUser(self, type='234'):
        container = UserContainer(type)
        container.checkUser(5, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(5, 'Morty', 'duwaerts', 'scared@gmail.com')
        container.checkUser(5, 'Ronan', 'Marvel', 'coolboy1452@uantwerpen.com')
        container.checkUser(5, 'Tina', 'Turner', 'power@gmail.com')
        container.checkUser(5, 'powerpuff', 'girl', 'pinklady@hotmail.com')
        container.checkUser(5, 'Rick', 'sanchez', 'getSchwifty@universe.com')
        container.checkUser(42, 'Arthur', 'Dent', 'still-flying@42life.com')
        container.checkUser(5, 'Time', 'Machine', 'time.machines@gmail.com')
        container.checkUser(28, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(12, 'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.checkUser(5, 'octo', 'ananas', 'at@gmail.com')
        container.checkUser(5, 'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        container.checkUser(5, 'Witchking-of', 'Angmar', 'barad.dur@mordor.be')

        self.assertEqual('Gintoki', container.retrieveUser("gin-sensei@gmail.com")[1].getFirstname())
        self.assertEqual('Angmar', container.retrieveUser("barad.dur@mordor.be")[1].getLastname())
        self.assertEqual([5, 28, 12],container.retrieveUser("gin-sensei@gmail.com")[1].getOrders())
        self.assertEqual([42],container.retrieveUser("still-flying@42life.com")[1].getOrders())
        self.assertEqual([5, 28, 12],container.retrieveUser("gin-sensei@gmail.com")[1].getOrders())

    def testIsEmpty(self, type='bs'):
        container = UserContainer(type)
        self.assertTrue(container.isEmpty())

        container.checkUser(5, 'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        self.assertFalse(container.isEmpty())
