# views/tkinter_view.py - Tkinter UI Implementation
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import OptionMenu
from tkcalendar import Calendar  # You need to install tkcalendar with `pip install tkcalendar`
from controller import StudyPlannerController

class StudyPlannerTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = StudyPlannerController()
        self.title("Study Planner - Tkinter")
        self.geometry("400x400")  # Increased height for calendar

        # Task Name Label & Entry
        self.label_task = tk.Label(self, text="Enter Task Name:")
        self.label_task.pack()
        self.entry_task = tk.Entry(self, width=30)
        self.entry_task.pack(pady=5)

        # Priority Label & Dropdown
        self.label_priority = tk.Label(self, text="Select Priority (1-5):")
        self.label_priority.pack()
        self.priority_var = tk.StringVar(value="1")  # Default priority is 1
        self.priority_dropdown = OptionMenu(self, self.priority_var, "1", "2", "3", "4", "5")
        self.priority_dropdown.pack(pady=5)

        # Deadline Label & Calendar
        self.label_deadline = tk.Label(self, text="Select Deadline:")
        self.label_deadline.pack()
        self.calendar = Calendar(self, date_pattern="yyyy-mm-dd")  # Calendar widget
        self.calendar.pack(pady=5)

        # Add Task Button
        self.btn_add = tk.Button(self, text="Add Task", command=self.add_task)
        self.btn_add.pack()

        # Task List Display
        self.task_listbox = tk.Listbox(self, width=50)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.entry_task.get()
        priority = self.priority_var.get()  # Get priority from dropdown
        deadline = self.calendar.get_date()  # Get selected date from calendar

        # Input Validation
        if not task:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return
        
        try:
            priority = int(priority)
            if not (1 <= priority <= 5):
                raise ValueError
        except ValueError:
            messagebox.showwarning("Warning", "Priority must be an integer between 1 and 5.")
            return
        
        self.controller.add_task(task, priority, deadline)
        self.update_task_list()
        self.entry_task.delete(0, tk.END)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.controller.get_tasks():
            self.task_listbox.insert(tk.END, f"{task[0]} (Priority: {task[1]}, Deadline: {task[2]})")

if __name__ == "__main__":
    app = StudyPlannerTkinter()
    app.mainloop()
