"""Project Part Three: object-oriented inventory management."""

from inventory import Inventory, Item
from inventory_data import create_inventory


def build_inventory():
    inventory = Inventory()
    for item_data in create_inventory():
        item = Item(
            item_data["name"],
            item_data["quantity"],
            item_data["price"],
            item_data["category"],
        )
        inventory.add_item(item)
    return inventory


def main():
    inventory = build_inventory()

    print("Nosh & Nibbles Inventory System")
    print()

    inventory.display_inventory()
    print()

    print(inventory.add_item(Item("Yogurt", 18, 2.79, "Dairy")))
    print(inventory.remove_item("Coffee"))
    print(inventory.update_item("Milk", quantity=32, price=3.25))
    print()

    found_item = inventory.find_by_name("Bread")
    if found_item:
        print("Search by name:")
        print(found_item)
        print()

    print("Search by category (Produce):")
    for item in inventory.search_by_category("Produce"):
        print(item)
    print()

    inventory.display_inventory()
    print()
    print(f"Total inventory value: ${inventory.total_inventory_value():.2f}")


if __name__ == "__main__":
    main()
