import unittest

from inventory import (
    add_item,
    calculate_total_value,
    grocery_inventory,
    low_stock_items,
    remove_item,
    update_quantity,
)


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = grocery_inventory.copy()

    def test_add_item_success(self):
        message = add_item(self.inventory, "Spinach", "Vegetable", 8, 2.25)
        self.assertEqual(message, "Spinach added to the inventory.")
        self.assertIn("Spinach", self.inventory)

    def test_add_item_duplicate(self):
        message = add_item(self.inventory, "Carrots", "Vegetable", 5, 1.50)
        self.assertEqual(message, "Carrots already exists in the inventory.")

    def test_update_quantity_success(self):
        message = update_quantity(self.inventory, "Corn", 6)
        self.assertEqual(message, "Updated Corn quantity to 10.")
        self.assertEqual(self.inventory["Corn"][1], 10)

    def test_update_quantity_missing_item(self):
        message = update_quantity(self.inventory, "Tomato", 3)
        self.assertEqual(message, "Tomato not found in the inventory.")

    def test_calculate_total_value(self):
        total_value = calculate_total_value(self.inventory)
        self.assertAlmostEqual(total_value, 89.0)

    def test_remove_item_success(self):
        message = remove_item(self.inventory, "Cucumber")
        self.assertEqual(message, "Cucumber removed from the inventory.")
        self.assertNotIn("Cucumber", self.inventory)

    def test_remove_item_missing_item(self):
        message = remove_item(self.inventory, "Tomato")
        self.assertEqual(message, "Tomato not found in the inventory.")

    def test_low_stock_items(self):
        low_stock = low_stock_items(self.inventory, threshold=5)
        self.assertEqual(low_stock, ["Corn"])


if __name__ == "__main__":
    unittest.main()
