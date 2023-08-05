import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    result_label.config(text=f"Selected Date: {selected_date}")

root = tk.Tk()
root.title("Calendar Date Picker")
root.geometry("300x300")

cal = Calendar(root, selectmode="day", year=2023, month=8, day=5)
cal.pack(pady=20)

select_button = ttk.Button(root, text="Select Date", command=get_date)
select_button.pack(pady=10)

result_label = ttk.Label(root, text="Selected Date:")
result_label.pack(pady=10)

root.mainloop()
