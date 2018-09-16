#!/bin/python3

import os
from collections import OrderedDict

month_by_days = OrderedDict([
    ('January', 31),
    ('February', 28),
    ('March', 31),
    ('April', 30),
    ('May', 31),
    ('June', 30),
    ('July', 31),
    ('August', 31),
    ('September', 30)
])

def dayOfProgrammer(year):
    day_counter = 256 if year != 1918 else 256 - 13
    if year <= 1917:
        day_counter -= 1 if year % 4 == 0 else 0
    else:
        day_counter -= 1 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 0
    for month_index, month in enumerate(month_by_days.items()):
        day_counter -= month[1]

        if day_counter <= 0:
            month_of_programmer_day = ('0' + str(month_index + 1))[-2:]
            programmer_day = ('0' + str(month[1] + day_counter))[-2:]
            return '%s.%s.%s' % (programmer_day, month_of_programmer_day, year)

        

if __name__ == '__main__':
    year = 1918#int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
    # with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
    #     fptr.write(str(result) + '\n')
