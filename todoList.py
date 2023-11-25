import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Todo List App")
root.resizable(False, False)

function_frame = tk.Frame(root)
function_frame.pack(pady=20)

entry = tk.Entry(function_frame, width=30, font=('Calibri', 12))
entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(function_frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(function_frame, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(function_frame, text="Clear All", width=10, command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5)

listbox = tk.Listbox(root, width=50, height=10, font=('Calibri', 12))
listbox.pack(padx=20, pady=10)

root.mainloop()
