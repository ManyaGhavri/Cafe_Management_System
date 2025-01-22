import tkinter as tk
from tkinter import messagebox

class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("700x600")  # Increased width for better layout
        self.root.configure(bg="#f5f5dc")  # Set background color

        # Menu items with prices
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 100,
            "Cake": 80,
            "Juice": 60,
            "Burger": 120,
            "Pizza": 200,
            "Pasta": 150,
            "Salad": 70,
            "Ice Cream": 90
        }

        self.order = {}

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Heading
        heading = tk.Label(self.root, text="Cafertia & Co", font=("Arial", 20, "bold"), bg="#f5f5dc", fg="#8b4513")
        heading.pack(pady=10)

        # Frames for layout
        top_frame = tk.Frame(self.root, bg="#f5f5dc")
        top_frame.pack(fill="x", padx=20, pady=5)

        middle_frame = tk.Frame(self.root, bg="#f5f5dc")
        middle_frame.pack(fill="x", padx=20, pady=5)

        bottom_frame = tk.Frame(self.root, bg="#f5f5dc")
        bottom_frame.pack(fill="x", padx=20, pady=5)

        # Menu Frame
        menu_frame = tk.LabelFrame(top_frame, text="Menu", font=("Arial", 12, "bold"), bg="#fffacd", fg="#8b4513")
        menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        for item, price in self.menu.items():
            tk.Label(menu_frame, text=f"{item} - ₹{price}", font=("Arial", 12), bg="#fffacd", fg="#000").pack(anchor="w")

        # Order Frame
        order_frame = tk.LabelFrame(top_frame, text="Order", font=("Arial", 12, "bold"), bg="#f0e68c", fg="#8b4513")
        order_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tk.Label(order_frame, text="Select Item:", font=("Arial", 12), bg="#f0e68c").grid(row=0, column=0, padx=10, pady=5)
        self.item_var = tk.StringVar()
        self.item_var.set("Select")
        item_menu = tk.OptionMenu(order_frame, self.item_var, *self.menu.keys())
        item_menu.config(bg="#dcdcdc", font=("Arial", 10))
        item_menu.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(order_frame, text="Number of Items:", font=("Arial", 12), bg="#f0e68c").grid(row=1, column=0, padx=10, pady=5)
        self.quantity_var = tk.IntVar()
        quantity_entry = tk.Entry(order_frame, textvariable=self.quantity_var, font=("Arial", 12), bg="#ffffff")
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        add_button = tk.Button(order_frame, text="Add to Order", command=self.add_to_order, font=("Arial", 12), bg="#8fbc8f", fg="#fff")
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Order Summary Frame
        summary_frame = tk.LabelFrame(middle_frame, text="Order Summary", font=("Arial", 12, "bold"), bg="#e6e6fa", fg="#8b4513")
        summary_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.summary_text = tk.Text(summary_frame, font=("Arial", 12), state="disabled", height=10, bg="#ffffff", fg="#000")
        self.summary_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(bottom_frame, bg="#f5f5dc")
        button_frame.pack(fill="x", pady=20)

        generate_bill_button = tk.Button(button_frame, text="Generate Bill", command=self.generate_bill, font=("Arial", 12), bg="#8b0000", fg="#fff")
        generate_bill_button.pack(side="left", padx=50)

        place_order_button = tk.Button(button_frame, text="Place Order", command=self.place_order, font=("Arial", 12), bg="#4682b4", fg="#fff")
        place_order_button.pack(side="right", padx=50)

    def add_to_order(self):
        item = self.item_var.get()
        quantity = self.quantity_var.get()

        if item == "Select" or quantity <= 0:
            messagebox.showerror("Error", "Please select a valid item and quantity.")
            return

        if item in self.order:
            self.order[item] += quantity
        else:
            self.order[item] = quantity

        self.update_summary()
        self.item_var.set("Select")
        self.quantity_var.set(0)

    def update_summary(self):
        self.summary_text.config(state="normal")
        self.summary_text.delete(1.0, tk.END)

        for item, quantity in self.order.items():
            self.summary_text.insert(tk.END, f"{item} x {quantity} = ₹{self.menu[item] * quantity}\n")

        self.summary_text.config(state="disabled")

    def generate_bill(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        messagebox.showinfo("Bill", f"Your total bill is: ₹{total}")

    def place_order(self):
        if not self.order:
            messagebox.showerror("Error", "No items in the order.")
            return

        self.generate_bill()
        self.order.clear()
        self.update_summary()
        messagebox.showinfo("Success", "Order placed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeManagementSystem(root)
    root.mainloop()
