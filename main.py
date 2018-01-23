#! /usr/bin/python3

import sys
from quetzal import *

quetzal = Quetzal()

if len(sys.argv) != 2:
    print('Usage: main.py system.txt')
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
    started = False
    for line in system:
        line = line.strip()
        # Ignore all lines that start with a hashtag.
        if line.startswith('#'):
            continue

        splits = line.split(' ')

        if not started:
            cmd = splits[0]

            if cmd == '':
                # Skip empty lines.
                continue
            elif cmd == 'init':
                # Initialize a new Quetzal object
                quetzal = Quetzal()
            elif cmd == 'shot':
                type_ = splits[1]
                amount = int(splits[2])
                exp_date = to_date(splits[3],splits[4],splits[5])

                for i in range(amount):
                    shot = Chocolateshot(exp_date, type_)
                    quetzal.add_to_stock(shot)

            elif cmd == 'honing':
                amount = int(splits[1])
                exp_date = to_date(splits[2], splits[3], splits[4])
                for i in range(amount):
                    honey = Honey(exp_date)
                    quetzal.add_to_stock(honey)
            elif cmd == 'marshmallow':
                amount = int(splits[1])
                exp_date = to_date(splits[2], splits[3], splits[4])
                for i in range(amount):
                    marshmallow = Marshmallow(exp_date)
                    quetzal.add_to_stock(marshmallow)
            elif cmd == 'chili':
                amount = int(splits[1])
                exp_date = to_date(splits[2], splits[3], splits[4])
                for i in range(amount):
                    chili = Chilipepper(exp_date)
                    quetzal.add_to_stock(chili)
            elif cmd == 'gebruiker':
                first_name = splits[1]
                last_name = splits[2]
                email = splits[3]

                quetzal.add_user(first_name, last_name, email)
            elif cmd == 'werknemer':
                first_name = splits[1]
                last_name = splits[2]
                workload = int(splits[3])

                quetzal.add_employee(first_name, last_name, workload)
            elif cmd == 'start':
                quetzal.start_system()
                started = True
        else:
            c = splits[0]
            if c == '':
                continue

            c = int(c)
            quetzal.run_until(c)

            cmd = splits[1]

            if cmd == 'bestel':
                email = splits[2]

                dt_index = len(splits) - 5

                year = splits[dt_index]
                month = splits[dt_index + 1]
                day = splits[dt_index + 2]

                date = to_date(year, month, day)

                hour = int(splits[dt_index + 3])
                minute = int(splits[dt_index + 4])

                datetime = DateTime(date, hour, minute)

                quetzal.place_order(email, splits[3:dt_index], datetime)

            elif cmd == 'stock':
                prod = splits[2]

                if prod == 'shot':
                    type_ = splits[3]
                    amount = int(splits[4])
                    exp_date = to_date(splits[5],splits[6],splits[7])

                    for i in range(amount):
                        shot = Chocolateshot(exp_date, type_)
                        quetzal.add_to_stock(shot)

                elif prod == 'honing':
                    amount = int(splits[3])
                    exp_date = to_date(splits[4], splits[5], splits[6])
                    for i in range(amount):
                        honey = Honey(exp_date)
                        quetzal.add_to_stock(honey)
                elif prod == 'marshmallow':
                    amount = int(splits[3])
                    exp_date = to_date(splits[4], splits[5], splits[6])
                    for i in range(amount):
                        marshmallow = Marshmallow(exp_date)
                        quetzal.add_to_stock(marshmallow)
                elif prod == 'chili':
                    amount = int(splits[3])
                    exp_date = to_date(splits[4], splits[5], splits[6])
                    for i in range(amount):
                        chili = Chilipepper(exp_date)
                        quetzal.add_to_stock(chili)
            elif cmd == 'log':
                quetzal.log()
