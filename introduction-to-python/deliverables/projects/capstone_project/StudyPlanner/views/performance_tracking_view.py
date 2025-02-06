# views/performance_tracking_view.py - Performance Tracking UI
import tkinter as tk
from tkinter import messagebox
from controller import StudyPlannerController
# from views.tkinter_view import StudyPlannerTkinter

class PerformanceTrackingView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = StudyPlannerController()
        self.title("Performance Tracking")
        self.geometry("400x350")

        # Subject Entry
        tk.Label(self, text="Enter Subject Name:").pack()
        self.entry_subject = tk.Entry(self, width=30)
        self.entry_subject.pack(pady=5)

        # Score Entry
        tk.Label(self, text="Enter Score (0-100):").pack()
        self.entry_score = tk.Entry(self, width=10)
        self.entry_score.pack(pady=5)

        # Add Score Button
        self.btn_add_score = tk.Button(self, text="Add Score", command=self.add_score)
        self.btn_add_score.pack()

        # View Performance Button
        self.btn_view_performance = tk.Button(self, text="View Averages", command=self.view_averages)
        self.btn_view_performance.pack(pady=5)

        # View All Scores Button
        self.btn_view_all_scores = tk.Button(self, text="View All Scores", command=self.view_all_scores)
        self.btn_view_all_scores.pack(pady=5)

        # Task Management Button
        self.btn_task_management = tk.Button(self, text="Manage Study Tasks", command=self.open_task_manager)
        self.btn_task_management.pack(pady=5)

        # Exit Button
        self.btn_exit = tk.Button(self, text="Exit", command=self.exit_application)
        self.btn_exit.pack(pady=5)

    def add_score(self):
        subject = self.entry_subject.get()
        score = self.entry_score.get()

        message = self.controller.add_score(subject, score)
        if "Error" in message:
            messagebox.showwarning("Warning", message)
        else:
            messagebox.showinfo("Success", message)

        self.entry_subject.delete(0, tk.END)
        self.entry_score.delete(0, tk.END)

    def view_averages(self):
        averages = self.controller.get_average_scores()
        if averages:
            avg_text = "\n".join([f"{subject}: {score:.2f}" for subject, score in averages.items()])
        else:
            avg_text = "No scores recorded yet."

        messagebox.showinfo("Average Scores", avg_text)

    def view_all_scores(self):
        """Opens a new window displaying all subjects and their scores."""
        all_scores = self.controller.get_all_scores()
        
        score_window = tk.Toplevel(self)
        score_window.title("All Scores")
        score_window.geometry("300x300")

        if not all_scores:
            tk.Label(score_window, text="No scores recorded yet.").pack()
            return

        for subject, scores in all_scores.items():
            tk.Label(score_window, text=f"{subject}: {', '.join(map(str, scores))}").pack()

    def open_task_manager(self):
        """Opens the Study Task Manager UI."""
        self.destroy()  # Close the main menu

        # ✅ Lazy Import to Avoid Circular Import
        from views.tkinter_view import StudyPlannerTkinter
        app = StudyPlannerTkinter()
        app.mainloop()

    def exit_application(self):
        """Ensures all Tkinter windows are properly closed."""
        self.destroy()  # ✅ Closes the window and any child windows
        self.quit()     # ✅ Ensures the event loop is fully stopped


if __name__ == "__main__":
    app = PerformanceTrackingView()
    app.mainloop()
