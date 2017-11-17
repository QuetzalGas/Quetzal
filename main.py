#! /bin/python3

import sys
from quetzal import *

quetzal = None

if len(sys.argv) != 2:
    print('No system.txt')
    exit()

def to_date(year, month, day):
    return Date(int(year), int(month), int(day))

def parse_ingredient(stgl):
    if stg[0] == 'shot':
        pass
    elif stg[0] == 'honing':
        pass
    elif stg[0] == 'marshmallow':
        pass
    elif stg[0] == 'chili':
        pass
    else:
        return None


with open(sys.argv[1]) as system:
    for line in system:
        line = line.strip()
        if line.startswith('#'):
            continue

        splits = line.split(' ')

        cmd = splits[0]

        if cmd == '':
            continue
        elif cmd == 'init':
            quetzal = Quetzal()
        elif cmd == 'shot':
            shot = ChocolateShot()
            count = 1
            quetzal.add_to_stock(shot, count)
        elif cmd == 'honing':
            honey = Honey()
            count = 1
            quetzal.add_to_stock(honey, count)
        elif cmd == 'marshmallow':
            marshmallow = Marshmallow()
            count = 1
            quetzal.add_to_stock(marshmallow, count)
        elif cmd == 'chili':
            chilipepper = Chilipepper()
            count = 1
            quetzal.add_to_stock(chilipepper, count)
        elif cmd == 'gebruiker':
            user = User()
            quetzal.add_user(user)
        elif cmd == 'werknemer':
            employee = Employee()
            quetzal.add_employee(employee)
        elif cmd == 'start':
            pass
