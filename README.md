## Reto 7- Queue
Se uso una cola FIFO en el ejercicio.

Aqui hay un ejemplo de uso:
```python
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
```

Un mejor Readme pronto.
