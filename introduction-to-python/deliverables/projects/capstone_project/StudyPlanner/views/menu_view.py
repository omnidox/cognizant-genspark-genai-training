# views/menu_view.py - Main Menu for Study Planner
import tkinter as tk
from views.tkinter_view import StudyPlannerTkinter
from views.performance_tracking_view import PerformanceTrackingView  # You'll create this later

class StudyPlannerMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Planner - Main Menu")
        self.geometry("400x250")

        tk.Label(self, text="Welcome to the Study Planner!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text="Choose an option below:", font=("Arial", 12)).pack(pady=5)

        # Task Management Button
        self.btn_task_management = tk.Button(self, text="Manage Study Tasks", command=self.open_task_manager)
        self.btn_task_management.pack(pady=5)

        # Performance Tracking Button
        self.btn_performance_tracking = tk.Button(self, text="Track Performance & Scores", command=self.open_performance_tracker)
        self.btn_performance_tracking.pack(pady=5)

        # Exit Button
        self.btn_exit = tk.Button(self, text="Exit", command=self.quit)
        self.btn_exit.pack(pady=5)

    def open_task_manager(self):
        """Opens the Study Task Manager UI."""
        self.destroy()  # Close the main menu
        app = StudyPlannerTkinter()  # Open Task Management View
        app.mainloop()

    def open_performance_tracker(self):
        """Opens the Performance Tracking UI."""
        self.destroy()  # Close the main menu
        app = PerformanceTrackingView()  # Open Performance Tracking View
        app.mainloop()

if __name__ == "__main__":
    app = StudyPlannerMenu()
    app.mainloop()
