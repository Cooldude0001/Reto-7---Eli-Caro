# Imports
from collections import namedtuple
from queue import Queue

class MenuItem:
    """Base class for menu items."""

    def __init__(self, name: str, price: float):
        """Initialize a MenuItem object with name and price parameters.

        - param name: Name of the MenuItem object.
        - param price: Price of the MenuItem object.
        """
        self._name = name
        self._price = price

    def get_name(self):
        """Return the name of the MenuItem object."""
        return self._name

    def set_name(self, name: str):
        """Set the name of the MenuItem object.

        - param name: New name to set.
        """
        self._name = name

    def get_price(self):
        """Return the price of the MenuItem object."""
        return self._price

    def set_price(self, price: float):
        """Set the price of the MenuItem object.

        - param price: New price to set.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = price

    def total_price(self, quantity: int = 1) -> float:
        """Calculate the total price based on quantity.

        - param quantity: Quantity of the MenuItem.
        - return: Total price as a float.
        """
        return self._price * quantity

    def __str__(self):
        """Return a string representation of the MenuItem object."""
        return f"{self._name} - ${self._price:.2f}"


class Beverage(MenuItem):
    """Beverage class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float, size: str):
        """Initialize a Beverage object with name, price, and size parameters.

        - param name: Name of the Beverage object.
        - param price: Price of the Beverage object.
        - param size: Size of the Beverage object (e.g., Small, Medium, Large).
        """
        super().__init__(name, price)
        self._size = size

    def get_size(self):
        """Return the size of the Beverage object."""
        return self._size

    def set_size(self, size: str):
        """Set the size of the Beverage object.

        - param size: New size to set.
        """
        self._size = size

    def __str__(self):
        """Return a string representation of the Beverage object."""
        return f"{self._name} - ${self._price:.2f} ({self._size})"


class Appetizer(MenuItem):
    """Appetizer class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float, portion_size: str):
        """Initialize an Appetizer object with name, price, and portion size.

        - param name: Name of the Appetizer object.
        - param price: Price of the Appetizer object.
        - param portion_size: Portion size of the Appetizer object (e.g., 6 pieces, 1 plate).
        """
        super().__init__(name, price)
        self._portion_size = portion_size

    def get_portion_size(self):
        """Return the portion size of the Appetizer object."""
        return self._portion_size

    def set_portion_size(self, portion_size: str):
        """Set the portion size of the Appetizer object.

        - param portion_size: New portion size to set.
        """
        self._portion_size = portion_size

    def __str__(self):
        """Return a string representation of the Appetizer object."""
        return f"{self._name} - ${self._price:.2f} ({self._portion_size})"


class Maincourse(MenuItem):
    """Maincourse class inherits methods and attributes from MenuItem class."""

    def __init__(self, name: str, price: float):
        """Initialize a Maincourse object with name and price parameters.

        - param name: Name of the Maincourse object.
        - param price: Price of the Maincourse object.
        """
        super().__init__(name, price)

    def __str__(self):
        """Return a string representation of the Maincourse object."""
        return f"{self._name} - ${self._price:.2f}"


class Order:
    """Order class is used to create and calculate the bill."""

    def __init__(self):
        """Initialize an Order with an empty list of items."""
        self._order_items = []

    def add_menu_item(self, item: MenuItem, quantity: int = 1):
        """Add a MenuItem object to the order.

        - param item: A MenuItem instance to be added.
        - param quantity: Quantity of the MenuItem to add.
        """
        self._order_items.append((item, quantity))

    def calculate_total_price(self) -> float:
        """Calculate the total bill with an optional discount for beverages.

        - return: Total price as a float.
        """
        total = 0
        has_maincourse = any(isinstance(item, Maincourse) for item, _ in self._order_items)

        for item, quantity in self._order_items:
            if has_maincourse and isinstance(item, Beverage):
                total += item.total_price(quantity) * 0.9  # 10% discount on beverages
            else:
                total += item.total_price(quantity)

        return total

    def __str__(self):
        """Return a string representation of the Order object."""
        return "\n".join(
            f"{quantity}x {item}" for item, quantity in self._order_items
        )


class Payment:
    """Base class for different payment methods."""

    def pay(self, amount: float):
        """Abstract method to process payment.

        - param amount: The amount to be paid.
        """
        raise NotImplementedError("Subclasses must implement the pay() method.")


class CardPayment(Payment):
    """Class for card payment method."""

    def __init__(self, card_number: str, cvv: int):
        """Initialize a CardPayment object.

        - param card_number: Card number for the payment.
        - param cvv: CVV code of the card.
        """
        self._card_number = card_number
        self._cvv = cvv

    def pay(self, amount: float):
        """Process the payment using a card.

        - param amount: The amount to be paid.
        """
        print(f"Paying ${amount:.2f} with card ending in {self._card_number[-4:]}")


class CashPayment(Payment):
    """Class for cash payment method."""

    def __init__(self, cash_given: float):
        """Initialize a CashPayment object.

        - param cash_given: The cash amount provided for payment.
        """
        self._cash_given = cash_given

    def pay(self, amount: float):
        """Process the payment using cash.

        - param amount: The amount to be paid.
        """
        if self._cash_given >= amount:
            change = self._cash_given - amount
            print(f"Paid ${amount:.2f} in cash. Change: ${change:.2f}")
        else:
            print(f"Insufficient funds. Need ${amount - self._cash_given:.2f} more.")


# Definition of the menu set using named tuple
MenuSet = namedtuple("MenuSet", ["Appetizer", "Maincourse", "Beverage"])

class OrderManager:
    """Class to manage multiple orders using a FIFO queue."""
    
    def __init__(self):
        """Initialize an OrderManager with an empty queue."""
        self._orders = Queue()
    
    def add_order(self, order):
        """Add an order to the queue."""
        self._orders.put(order)
    
    def process_order(self):
        """Process and remove the first order from the queue."""
        if not self._orders.empty():
            return self._orders.get()
        return None
    
    def __len__(self):
        """Return the number of orders in the queue."""
        return self._orders.qsize()

class Menu:
    """Class to manage MenuItems stored in a Python dictionaries."""
    
    def __init__(self):
        """Initialize the Menu class with an empty menu."""
        self.menu_items = {}
    
    def add_item(self, category, name, price):
        """Add a new item to the menu under a specific category."""
        if category not in self.menu_items:
            self.menu_items[category] = []
        self.menu_items[category].append({"name": name, "price": price})
    
    def update_item(self, category, old_name, new_name, new_price):
        """Update an existing item in the menu."""
        if category in self.menu_items:
            for item in self.menu_items[category]:
                if item["name"] == old_name:
                    item["name"] = new_name
                    item["price"] = new_price
                    return True
        return False
    
    def delete_item(self, category, name):
        """Delete an item from the menu."""
        if category in self.menu_items:
            self.menu_items[category] = [
            item for item in self.menu_items[category] if item["name"] != name]
            return True
        return False
    
    def get_menu(self):
        """Return the actual menu data."""
        return self.menu_items

# Example usage
menu = Menu()
menu.add_item("Beverage", "Coke", 2.5)
menu.add_item("Appetizer", "Spring Rolls", 5.0)
menu.add_item("Maincourse", "Spaghetti", 12.0)

# Show the actual menu
print("Actual menu:", menu.get_menu())

# Create an order and adding them to the menu
order1 = Order()
order1.add_menu_item(MenuItem("Coke", 2.5), 2)  # 2 Cokes
order1.add_menu_item(MenuItem("Spring Rolls", 5.0), 1)  # 1 Spring Roll
order1.add_menu_item(MenuItem("Spaghetti", 12.0), 1)  # 1 Spaghetti

order2 = Order()
order2.add_menu_item(MenuItem("Coke", 2.5), 1)  # 1 Coke
order2.add_menu_item(MenuItem("Spring Rolls", 5.0), 2)  # 2 Spring Rolls

# Using the OrderManager class to manage the orders
order_manager = OrderManager()
order_manager.add_order(order1)
order_manager.add_order(order2)

# Process orders in order
while len(order_manager) > 0:
    processed_order = order_manager.process_order()
    if processed_order:
        print("\processed order:")
        print(processed_order)
        print(f"Total to pay: ${processed_order.calculate_total_price():.2f}")