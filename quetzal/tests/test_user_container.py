from unittest import TestCase
from quetzal.user import UserContainer
from quetzal import *

class TestUserContainer(TestCase):
    def setUp(self):
        self.type = AdtTwoThreeTree()
    def testadd_if_unknown_user(self):
        container = UserContainer(self.type)
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user('Morty', 'duwaerts', 'scared@gmail.com')
        container.add_if_unknown_user(
            'Ronan', 'Marvel', 'coolboy1452@uantwerpen.com')
        container.add_if_unknown_user('Tina', 'Turner', 'power@gmail.com')
        container.add_if_unknown_user(
            'powerpuff', 'girl', 'pinklady@hotmail.com')
        container.add_if_unknown_user(
            'Rick', 'sanchez', 'getSchwifty@universe.com')
        container.add_if_unknown_user(
            'Arthur', 'Dent', 'still-flying@42life.com')
        container.add_if_unknown_user(
            'Time', 'Machine', 'time.machines@gmail.com')
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user('octo', 'ananas', 'at@gmail.com')
        container.add_if_unknown_user(
            'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        container.add_if_unknown_user(
            'Witchking-of', 'Angmar', 'barad.dur@mordor.be')

    def testretrieve_user(self):
        container = UserContainer(self.type)
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user('Morty', 'duwaerts', 'scared@gmail.com')
        container.add_if_unknown_user(
            'Ronan', 'Marvel', 'coolboy1452@uantwerpen.com')
        container.add_if_unknown_user('Tina', 'Turner', 'power@gmail.com')
        container.add_if_unknown_user(
            'powerpuff', 'girl', 'pinklady@hotmail.com')
        container.add_if_unknown_user(
            'Rick', 'sanchez', 'getSchwifty@universe.com')
        container.add_if_unknown_user(
            'Arthur', 'Dent', 'still-flying@42life.com')
        container.add_if_unknown_user(
            'Time', 'Machine', 'time.machines@gmail.com')
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user(
            'Gintoki', 'Sakata', 'gin-sensei@gmail.com')
        container.add_if_unknown_user('octo', 'ananas', 'at@gmail.com')
        container.add_if_unknown_user(
            'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        container.add_if_unknown_user(
            'Witchking-of', 'Angmar', 'barad.dur@mordor.be')

        self.assertEqual('Gintoki', container.retrieve_user(
            "gin-sensei@gmail.com")[1].get_firstname())
        self.assertEqual('Angmar', container.retrieve_user(
            "barad.dur@mordor.be")[1].get_lastname())
        self.assertEqual('Sakata', container.retrieve_user(
            "gin-sensei@gmail.com")[1].get_lastname())
        self.assertEqual(6, container.retrieve_user(
            "still-flying@42life.com")[1].get_id())
        self.assertEqual(0, container.retrieve_user(
            "gin-sensei@gmail.com")[1].get_id())

    def testIsEmpty(self):
        container = UserContainer(self.type)
        self.assertTrue(container.is_empty())

        container.add_if_unknown_user(
            'Gimli', 'Something', 'minesOfmoria@farlindon.com')
        self.assertFalse(container.is_empty())

    def test_wrong_type(self):
        raised = False
        try:
            UserContainer("hey")
        except:
            raised = True
        self.assertTrue(raised)