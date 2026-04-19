"""Tkinter grocery application for Nosh & Nibbles."""

from tkinter import *
from tkinter import messagebox, ttk

from inventory_data import create_inventory


class GroceryApp:
    """Build and manage the grocery store checkout window."""

    def __init__(self, root):
        self.root = root
        self.root.title("Nosh & Nibbles Grocery Manager")
        self.root.geometry("860x540")

        self.inventory = sorted(create_inventory(), key=lambda item: item["name"])
        self.cart = []
        self.category_names = sorted(
            {item["category"] for item in self.inventory}
        )

        self.selected_item = StringVar()
        self.selected_category = StringVar()
        self.quantity = StringVar(value="1")
        self.status_text = StringVar(value="Ready to begin a new order.")
        self.total_items_text = StringVar(value="Total items in cart: 0")
        self.total_cost_text = StringVar(value="Order total: $0.00")

        self._create_menu()
        self._build_layout()
        self._load_defaults()
        self._refresh_item_options()

    def _create_menu(self):
        menu_bar = Menu(self.root)

        order_menu = Menu(menu_bar, tearoff=0)
        order_menu.add_command(label="New Order", command=self.new_order)
        order_menu.add_command(label="Clear Cart", command=self.clear_cart)
        order_menu.add_separator()
        order_menu.add_command(label="Exit", command=self.root.destroy)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menu_bar.add_cascade(label="Order", menu=order_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menu_bar)

    def _build_layout(self):
        mainframe = ttk.Frame(self.root, padding="14 14 14 14")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.rowconfigure(1, weight=1)

        title_label = ttk.Label(
            mainframe,
            text="Nosh & Nibbles Inventory and Checkout",
            font=("Segoe UI", 16, "bold"),
        )
        title_label.grid(column=0, row=0, columnspan=2, sticky=W, pady=(0, 12))

        input_frame = ttk.LabelFrame(mainframe, text="Add Item to Cart", padding="12 12 12 12")
        input_frame.grid(column=0, row=1, sticky=(N, W, E, S), padx=(0, 8))

        ttk.Label(input_frame, text="Category").grid(column=0, row=0, sticky=W)
        self.category_combo = ttk.Combobox(
            input_frame,
            textvariable=self.selected_category,
            state="readonly",
            width=24,
        )
        self.category_combo.grid(column=1, row=0, sticky=(W, E))
        self.category_combo.bind("<<ComboboxSelected>>", self._on_category_change)

        ttk.Label(input_frame, text="Item").grid(column=0, row=1, sticky=W)
        self.item_combo = ttk.Combobox(
            input_frame,
            textvariable=self.selected_item,
            state="readonly",
            width=24,
        )
        self.item_combo.grid(column=1, row=1, sticky=(W, E))

        ttk.Label(input_frame, text="Quantity").grid(column=0, row=2, sticky=W)
        quantity_entry = ttk.Entry(
            input_frame,
            textvariable=self.quantity,
            width=10,
        )
        quantity_entry.grid(column=1, row=2, sticky=W)

        ttk.Button(input_frame, text="Add to Cart", command=self.add_to_cart).grid(
            column=0, row=3, sticky=W, pady=(10, 0)
        )
        ttk.Button(input_frame, text="Clear Cart", command=self.clear_cart).grid(
            column=1, row=3, sticky=E, pady=(10, 0)
        )

        inventory_frame = ttk.LabelFrame(
            mainframe, text="Available Inventory", padding="12 12 12 12"
        )
        inventory_frame.grid(column=0, row=2, sticky=(N, W, E, S), padx=(0, 8), pady=(12, 0))
        inventory_frame.columnconfigure(0, weight=1)
        inventory_frame.rowconfigure(0, weight=1)

        self.inventory_listbox = Listbox(inventory_frame, height=10, width=42)
        self.inventory_listbox.grid(column=0, row=0, sticky=(N, W, E, S))
        self._populate_inventory_list()

        cart_frame = ttk.LabelFrame(mainframe, text="Current Cart", padding="12 12 12 12")
        cart_frame.grid(column=1, row=1, rowspan=2, sticky=(N, W, E, S))
        cart_frame.columnconfigure(0, weight=1)
        cart_frame.rowconfigure(0, weight=1)

        self.cart_listbox = Listbox(cart_frame, height=18, width=48)
        self.cart_listbox.grid(column=0, row=0, sticky=(N, W, E, S))

        totals_frame = ttk.Frame(cart_frame)
        totals_frame.grid(column=0, row=1, sticky=(W, E), pady=(12, 0))
        totals_frame.columnconfigure(0, weight=1)

        ttk.Label(totals_frame, textvariable=self.total_items_text).grid(column=0, row=0, sticky=W)
        ttk.Label(totals_frame, textvariable=self.total_cost_text).grid(column=0, row=1, sticky=W)
        ttk.Label(totals_frame, textvariable=self.status_text, foreground="navy").grid(
            column=0, row=2, sticky=W, pady=(8, 0)
        )

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        for child in input_frame.winfo_children():
            child.grid_configure(padx=4, pady=4)

    def _load_defaults(self):
        if self.category_names:
            self.selected_category.set(self.category_names[0])

    def _populate_inventory_list(self):
        self.inventory_listbox.delete(0, END)
        for item in self.inventory:
            display_text = (
                f"{item['name']} | {item['category']} | ${item['price']:.2f}"
            )
            self.inventory_listbox.insert(END, display_text)

    def _refresh_item_options(self):
        category = self.selected_category.get()
        matching_items = [
            item["name"] for item in self.inventory if item["category"] == category
        ]

        self.item_combo["values"] = matching_items
        if matching_items:
            self.selected_item.set(matching_items[0])
        else:
            self.selected_item.set("")

    def _on_category_change(self, _event=None):
        self._refresh_item_options()

    def _get_inventory_item(self, item_name):
        for item in self.inventory:
            if item["name"] == item_name:
                return item
        return None

    def add_to_cart(self):
        item_name = self.selected_item.get().strip()
        category = self.selected_category.get().strip()
        quantity_text = self.quantity.get().strip()

        if not item_name or not category:
            messagebox.showerror("Missing Information", "Please select a category and item.")
            return

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Quantity",
                "Quantity must be a whole number greater than zero.",
            )
            return

        inventory_item = self._get_inventory_item(item_name)
        if inventory_item is None:
            messagebox.showerror("Item Not Found", "The selected item is not in inventory.")
            return

        line_total = quantity * inventory_item["price"]
        cart_entry = {
            "name": item_name,
            "category": category,
            "quantity": quantity,
            "price": inventory_item["price"],
            "line_total": line_total,
        }
        self.cart.append(cart_entry)
        self._refresh_cart_display()

        self.status_text.set(f"Added {quantity} {item_name}(s) to the cart.")
        self.quantity.set("1")

    def _refresh_cart_display(self):
        self.cart_listbox.delete(0, END)

        total_items = 0
        total_cost = 0.0

        for entry in self.cart:
            total_items += entry["quantity"]
            total_cost += entry["line_total"]
            display_text = (
                f"{entry['name']} | {entry['category']} | Qty: {entry['quantity']} | "
                f"${entry['line_total']:.2f}"
            )
            self.cart_listbox.insert(END, display_text)

        self.total_items_text.set(f"Total items in cart: {total_items}")
        self.total_cost_text.set(f"Order total: ${total_cost:.2f}")

    def clear_cart(self):
        self.cart.clear()
        self.cart_listbox.delete(0, END)
        self.total_items_text.set("Total items in cart: 0")
        self.total_cost_text.set("Order total: $0.00")
        self.status_text.set("Cart cleared.")

    def new_order(self):
        self.clear_cart()
        self.quantity.set("1")
        self._load_defaults()
        self._refresh_item_options()
        self.status_text.set("Started a new order.")

    def show_about(self):
        messagebox.showinfo(
            "About Nosh & Nibbles",
            "Nosh & Nibbles Grocery Manager\nBuilt with Tkinter for inventory and checkout practice.",
        )


def main():
    root = Tk()
    GroceryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
