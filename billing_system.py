import tkinter as tk
from tkinter import messagebox

# Function to add item and price
def add_item():
    item_name = entry_item.get()
    item_price = entry_price.get()
    
    if item_name == "" or item_price == "":
        messagebox.showwarning("Input Error", "Please enter both item name and price")
    else:
        try:
            item_price = float(item_price)
            listbox_items.insert(tk.END, f"{item_name} - ${item_price:.2f}")
            total_price.set(total_price.get() + item_price)
            entry_item.delete(0, tk.END)
            entry_price.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid price")

# Function to clear the list and reset
def clear_all():
    listbox_items.delete(0, tk.END)
    total_price.set(0.0)

# Function to generate the bill (show total price)
def generate_bill():
    if listbox_items.size() == 0:
        messagebox.showwarning("No Items", "No items in the list to generate a bill")
    else:
        bill_details = "Items:\n"
        for item in listbox_items.get(0, tk.END):
            bill_details += item + "\n"
        bill_details += f"\nTotal Price: ${total_price.get():.2f}"
        messagebox.showinfo("Bill Generated", bill_details)

# Creating the main window
root = tk.Tk()
root.title("Billing System")

# Creating the input fields and labels
label_item = tk.Label(root, text="Enter Item Name:")
label_item.grid(row=0, column=0)

entry_item = tk.Entry(root)
entry_item.grid(row=0, column=1)

label_price = tk.Label(root, text="Enter Price:")
label_price.grid(row=1, column=0)

entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

# Creating buttons for adding item, generating bill, and clearing list
button_add = tk.Button(root, text="Add Item", command=add_item)
button_add.grid(row=2, column=0, columnspan=2)

button_generate = tk.Button(root, text="Generate Bill", command=generate_bill)
button_generate.grid(row=3, column=0, columnspan=2)

button_clear = tk.Button(root, text="Clear All", command=clear_all)
button_clear.grid(row=4, column=0, columnspan=2)

# Creating a listbox to display added items
listbox_items = tk.Listbox(root, width=50, height=10)
listbox_items.grid(row=5, column=0, columnspan=2)

# Creating a label to display total price
label_total = tk.Label(root, text="Total Price: $")
label_total.grid(row=6, column=0)

total_price = tk.DoubleVar()
total_price.set(0.0)
label_total_value = tk.Label(root, textvariable=total_price)
label_total_value.grid(row=6, column=1)

# Running the main loop
root.mainloop()
