from inventory import add_item, calculate_total_value, grocery_inventory
from inventory import low_stock_items, remove_item, update_quantity


def main():
    inventory = grocery_inventory.copy()

    print("Vegetable inventory project")
    print()

    print("Starting inventory:")
    for item_name, details in inventory.items():
        print(item_name, details)
    print()

    print(add_item(inventory, "Spinach", "Vegetable", 8, 2.25))
    print(update_quantity(inventory, "Corn", 6))
    print(remove_item(inventory, "Cucumber"))
    print(f"Low stock items: {low_stock_items(inventory, threshold=10)}")
    print(f"Total inventory value: ${calculate_total_value(inventory):.2f}")
    print()

    print("Updated inventory:")
    for item_name, details in inventory.items():
        print(item_name, details)


if __name__ == "__main__":
    main()
