import tkinter as tk
from tkinter import messagebox
#Main Logic
def calculate():
    try:
        #Getting the input
        loan_amount = float(entry_amount.get())
        rate = float(entry_rate.get())
        years = float(entry_years.get())

        #Math formula
        months = years * 12
        monthly_rate = (rate / 12) / 100

        if monthly_rate == 0:
            emi = loan_amount / months
        else:
            numerator = loan_amount * monthly_rate * ((1 + monthly_rate) ** months)
            denominator = ((1 + monthly_rate) ** months) - 1
            emi = numerator / denominator

        #Result
        label_result.config(text=f"Monthly EMI: {round(emi, 2)}")

    except ValueError:
        messagebox.showerror("Error", "Please enter proper input.")

#Graphical User Interface(GUI)

root = tk.Tk()
root.title("Simple EMI Calculator")
root.geometry("300x350")

# Labels and Boxes
tk.Label(root, text="Loan Amount:").pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Interest Rate (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Years:").pack(pady=5)
entry_years = tk.Entry(root)
entry_years.pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate, bg="lightblue").pack(pady=15)

# Result
label_result = tk.Label(root, text="EMI will appear here", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

root.mainloop()
