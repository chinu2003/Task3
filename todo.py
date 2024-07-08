import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Main program starts here
if __name__ == "__main__":
    # Setting up the main window
    window = tk.Tk()
    window.title("To-Do List")

    # Creating the frame for task entry
    task_frame = tk.Frame(window)
    task_frame.pack(pady=10)

    # Entry widget for task input
    task_entry = tk.Entry(task_frame, width=40)
    task_entry.pack(side=tk.LEFT, padx=10)

    # Add task button
    add_task_button = tk.Button(task_frame, text="Add Task", command=add_task)
    add_task_button.pack(side=tk.LEFT)

    # Listbox to display tasks
    tasks_listbox = tk.Listbox(window, width=50, height=15, selectmode=tk.SINGLE)
    tasks_listbox.pack(pady=20)

    # Frame for buttons to manage tasks
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # Delete task button
    delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
    delete_task_button.pack(side=tk.LEFT, padx=10)

    # Clear tasks button
    clear_tasks_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks)
    clear_tasks_button.pack(side=tk.LEFT)

    # Start the GUI event loop
    window.mainloop()
