import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    """
    Calculates BMI based on user input and displays the result with category.
    """
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())
        height_m = height_cm / 100
        bmi = weight_kg / (height_m**2)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


def classify_bmi(bmi):
    """
    Returns BMI category based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(
    row=2, column=0, columnspan=2, pady=10
)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
