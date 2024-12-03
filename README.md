# Menu
This project will get you used to working with Python classes. You'll write a program that lets a user order things off of a menu; the main "objects" you're working with, menus and orders, will be represented by the Python classes Menu and Order.

This project has three parts, each one building off the previous parts:

    The Menu class and its helper class, MenuItem.
    The Order class and its helper class, OrderItem.
    A program that ties it all together.

First, we'll need to be able to represent a menu. Create the file menu.py and write the following classes in that file.

The MenuItem class is a simple class that represents a single item on a menu. It has two attributes: name (a str) and price (a float). The MenuItem constructor takes those two arguments (name and price) in that order.

The Menu class stores a list of MenuItems, and has some member functions to make working with menus easier:

    __init__() takes no arguments, and creates an empty menu.
    add(name, price) takes two arguments: a name and a price. If an item with that name is not already present in the menu, it adds a new MenuItem for the new item to the end of the menu. If an item with that name already exists, it updates the item's price.
    find(name) takes one argument: a name. It tries to find a MenuItem in the menu with that name. If it exists, it returns that MenuItem. Otherwise, it returns None.

The next step is to be able to represent what a user orders off of a menu. Make a file called order.py, and in this file, write the following classes.

The OrderItem class is similar to the MenuItem class. It's a simple helper class for storing information about part of an order. It has two attributes: menuitem (a MenuItem) and quantity (an int). Its constructor takes those two arguments in that order; if quantity isn't specified, it defaults to one.

The Order class stores a list of OrderItems, and, like a Menu, has member functions that handle common Order operations:

    __init__() takes no arguments, and creates an empty order.
    add(menuitem, quantity) takes one or two arguments: a MenuItem and maybe an int. If the order doesn't contain any of that menu item yet, it adds a new OrderItem to the end of the order. If the order does contain that menu item, it adjusts the existing quantity. If quantity isn't specified, it defaults to one.
    total_price() takes no arguments, and returns the total price of the order as a float.
    total_quantity() takes no arguments, and returns the number of menu items in the order as an int (an order item with a quantity of three counts as three menu items).

Now that you have your menu and order types, you can use them to make a program that lets people order off a menu. Write it in a file called main.py. You'll want to import the Menu and Order classes that you wrote earlier; that code will be doing most of the work. See the Notes section for more on importing.

Your program should take exactly one command line argument. This argument is the path to a TSV file (the format is described below). When the program starts, it should load the menu described in this file, print it (followed by a newline), and then ask the user to order:
    
