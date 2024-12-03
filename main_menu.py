
from menu import MenuItem
from menu import Menu
from order import OrderItem
from order import Order

import sys

if len(sys.argv) == 2:
    menu_tsv = open(sys.argv[1], 'r')
    menu = Menu()
    count = 0
    for line in menu_tsv:
        data = line.strip().split('\t')
        count += 1
        if count == 1:
            continue
        else:
            menu.add(data[0], float(data[1])) 
    menu.print()
    print('')
    print('What would you like to order?', end='')
    comp_order = Order()
    order_placed = False
    for line in sys.stdin:
        line = line.strip()
        if any(item.name == line for item in menu.items): # check the line is in the menu 
            menuitem = next(item for item in menu.items if item.name == line)
            comp_order.add(menuitem)
            order_placed = True
        elif line == '':
            continue
        else:
            print('')
            print(f'Sorry, "{line}" isn\'t on the menu.', end='') 
    if order_placed == False:
        print('')
        sys.exit
    else:
        print('\n')
        comp_order.print()
        sys.exit()
else:
    print("USAGE: main.py menu.tsv")
    sys.exit()

