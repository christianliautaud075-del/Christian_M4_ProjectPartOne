# I changed the inventory from fruit to vegetables.
# I also added a way to remove items.
# Last, I added a function to show low stock items.

grocery_inventory = {
    "Carrots": ("Vegetable", 10, 1.50),
    "Cucumber": ("Vegetable", 10, 1.30),
    "Lettuce": ("Vegetable", 20, 1.75),
    "Corn": ("Vegetable", 4, 1.50),
    "Potato": ("Vegetable", 20, 1.00),
}


def add_item(inventory, item_name, category, quantity, price):
    if item_name in inventory:
        return f"{item_name} already exists in the inventory."
    else:
        inventory[item_name] = (category, quantity, price)
        return f"{item_name} added to the inventory."


def update_quantity(inventory, item_name, quantity):
    if item_name in inventory:
        category, current_quantity, price = inventory[item_name]
        inventory[item_name] = (category, current_quantity + quantity, price)
        return f"Updated {item_name} quantity to {inventory[item_name][1]}."
    else:
        return f"{item_name} not found in the inventory."


def calculate_total_value(inventory):
    total_value = 0
    for details in inventory.values():
        total_value += details[1] * details[2]
    return total_value


def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]
        return f"{item_name} removed from the inventory."
    else:
        return f"{item_name} not found in the inventory."


def low_stock_items(inventory, threshold=5):
    low_stock = []
    for item_name, details in inventory.items():
        if details[1] <= threshold:
            low_stock.append(item_name)
    return low_stock
