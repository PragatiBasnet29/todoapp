import tkinter as tk
from tkinter import messagebox, font

# Initialize the main app window
app = tk.Tk()
app.title("To-Do List")
app.geometry("450x500")
app.config(bg="#f0f4f8")

# Set custom fonts and colors
header_font = font.Font(family="Helvetica", size=18, weight="bold")
task_font = font.Font(family="Arial", size=12)
button_color = "#4CAF50"
button_hover_color = "#45a049"
task_complete_color = "#2e8b57"

# Task list to hold tasks
todo_list = []


# Functions to manage tasks
def add_task():
    """Add a new task with a checkbox to mark as completed."""
    task_text = entry_task.get()
    if task_text:
        task_var = tk.BooleanVar()
        task_frame = tk.Frame(app, bg="#f0f4f8", padx=5, pady=3)

        checkbox = tk.Checkbutton(
            task_frame,
            text=task_text,
            variable=task_var,
            command=lambda: toggle_complete(task_var, checkbox),
            font=task_font,
            bg="#f0f4f8",
            fg="black",
            selectcolor="white",
            activeforeground=button_color
        )

        checkbox.pack(anchor="w", pady=2)
        todo_list.append({"task": task_text, "completed": task_var, "frame": task_frame})
        task_frame.pack(anchor="w", padx=10, pady=5)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")


def toggle_complete(task_var, checkbox):
    """Update the checkbox color when the task is marked complete or incomplete."""
    if task_var.get():
        checkbox.config(fg=task_complete_color, font=task_font)
    else:
        checkbox.config(fg="black", font=task_font)


def delete_completed_tasks():
    """Delete all completed tasks from the list."""
    global todo_list
    todo_list = [task for task in todo_list if not task["completed"].get()]
    update_task_list()


def update_task_list():
    """Refresh the display of tasks."""
    for widget in app.winfo_children():
        if isinstance(widget, tk.Frame) and widget != frame_task:
            widget.destroy()
    for task in todo_list:
        task["frame"].pack(anchor="w", padx=10, pady=5)


def on_hover(button, color):
    """Change button color on hover."""
    button.config(bg=color)


# Header
header = tk.Label(app, text="My Stylish To-Do List", font=header_font, bg="#f0f4f8", fg=button_color)
header.pack(pady=10)

# Entry and buttons frame
frame_task = tk.Frame(app, bg="#f0f4f8")
frame_task.pack(pady=15)

# Entry for new tasks
entry_task = tk.Entry(frame_task, width=35, font=task_font, relief="solid", bd=1)
entry_task.pack(side=tk.LEFT, padx=10)

# Add Task button
button_add_task = tk.Button(frame_task, text="Add Task", command=add_task, font=task_font, bg=button_color, fg="white",
                            relief="flat", padx=10, pady=5)
button_add_task.pack(side=tk.LEFT)
button_add_task.bind("<Enter>", lambda e: on_hover(button_add_task, button_hover_color))
button_add_task.bind("<Leave>", lambda e: on_hover(button_add_task, button_color))

# Delete Completed Tasks button
button_delete_task = tk.Button(app, text="Delete Completed Tasks", command=delete_completed_tasks, font=task_font,
                               bg=button_color, fg="white", relief="flat", padx=15, pady=5)
button_delete_task.pack(pady=20)
button_delete_task.bind("<Enter>", lambda e: on_hover(button_delete_task, button_hover_color))
button_delete_task.bind("<Leave>", lambda e: on_hover(button_delete_task, button_color))

# Run the main loop
app.mainloop()
