import tkinter as tk
from tkinter import messagebox

class PettyFundApp:
    def __init__(self, root):
        self.balance = 0.0
        self.transactions = []  # List to store transaction history
        self.root = root
        self.root.title("Petty Fund System")
        
        # Label to show balance
        self.balance_label = tk.Label(root, text=f"Total Petty Fund Balance: ₱{self.balance:.2f}", font=('Arial', 14))
        self.balance_label.pack(pady=10)
        
        # Entry and button for cash-in
        self.cash_in_label = tk.Label(root, text="Enter amount to cash in:")
        self.cash_in_label.pack(pady=5)
        self.cash_in_entry = tk.Entry(root, width=20)
        self.cash_in_entry.pack(pady=5)
        
        # Description for cash-in
        self.description_label = tk.Label(root, text="Enter description:")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(root, width=30)
        self.description_entry.pack(pady=5)
        
        self.cash_in_button = tk.Button(root, text="Cash In", command=self.cash_in)
        self.cash_in_button.pack(pady=5)
        
        # Entry and button for cash-out
        self.cash_out_label = tk.Label(root, text="Enter amount to cash out:")
        self.cash_out_label.pack(pady=5)
        self.cash_out_entry = tk.Entry(root, width=20)
        self.cash_out_entry.pack(pady=5)
        
        # Description for cash-out
        self.cash_out_description_label = tk.Label(root, text="Enter description:")
        self.cash_out_description_label.pack(pady=5)
        self.cash_out_description_entry = tk.Entry(root, width=30)
        self.cash_out_description_entry.pack(pady=5)
        
        self.cash_out_button = tk.Button(root, text="Cash Out", command=self.cash_out)
        self.cash_out_button.pack(pady=5)
        
        # Button to show balance
        self.show_balance_button = tk.Button(root, text="Show Balance", command=self.show_balance)
        self.show_balance_button.pack(pady=10)
        
        # Transaction history
        self.history_label = tk.Label(root, text="Transaction History:", font=('Arial', 12))
        self.history_label.pack(pady=10)
        
        self.history_box = tk.Listbox(root, width=50, height=10)
        self.history_box.pack(pady=5)
        
    def cash_in(self):
        try:
            amount = float(self.cash_in_entry.get())
            description = self.description_entry.get()
            
            if amount <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a positive amount.")
            else:
                self.balance += amount
                self.update_balance_label()
                self.record_transaction(f"Cash In: ₱{amount:.2f}", description)
                messagebox.showinfo("Success", f"Successfully added ₱{amount:.2f} to the petty fund.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        finally:
            self.cash_in_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

    def cash_out(self):
        try:
            amount = float(self.cash_out_entry.get())
            description = self.cash_out_description_entry.get()
            
            if amount <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a positive amount.")
            elif amount > self.balance:
                messagebox.showwarning("Insufficient Funds", "Insufficient funds in the petty fund.")
            else:
                self.balance -= amount
                self.update_balance_label()
                self.record_transaction(f"Cash Out: ₱{amount:.2f}", description)
                messagebox.showinfo("Success", f"Successfully withdrew ₱{amount:.2f} from the petty fund.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        finally:
            self.cash_out_entry.delete(0, tk.END)
            self.cash_out_description_entry.delete(0, tk.END)

    def show_balance(self):
        messagebox.showinfo("Balance", f"Total Petty Fund Balance: ₱{self.balance:.2f}")

    def update_balance_label(self):
        self.balance_label.config(text=f"Total Petty Fund Balance: ₱{self.balance:.2f}")

    def record_transaction(self, transaction, description):
        # Record the transaction with the description
        full_transaction = f"{transaction} - {description}"
        self.transactions.append(full_transaction)
        self.history_box.insert(tk.END, full_transaction)

# Create the main window
root = tk.Tk()

# Initialize the PettyFundApp
app = PettyFundApp(root)

# Run the tkinter event loop
root.mainloop()
