# views/pyqt_view.py - PyQt UI Implementation
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
import sys
from controller import StudyPlannerController

class StudyPlannerPyQt(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = StudyPlannerController()
        self.setWindowTitle("Study Planner - PyQt")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.entry_task = QLineEdit(self)
        layout.addWidget(self.entry_task)

        self.entry_priority = QLineEdit(self)
        layout.addWidget(self.entry_priority)

        self.entry_deadline = QLineEdit(self)
        layout.addWidget(self.entry_deadline)

        self.add_button = QPushButton("Add Task", self)
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.task_listbox = QListWidget(self)
        layout.addWidget(self.task_listbox)

        self.setLayout(layout)

    def add_task(self):
        task = self.entry_task.text()
        priority = int(self.entry_priority.text())
        deadline = self.entry_deadline.text()

        if task:
            self.controller.add_task(task, priority, deadline)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def update_task_list(self):
        self.task_listbox.clear()
        for task in self.controller.get_tasks():
            self.task_listbox.addItem(f"{task[0]} (Priority: {task[1]}, Deadline: {task[2]})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudyPlannerPyQt()
    window.show()
    sys.exit(app.exec())
