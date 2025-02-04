from datetime import datetime 

# model.py - Study Planner Core Logic (Independent of GUI)
class StudyPlannerModel:
    def __init__(self):
        self.tasks = []  # List of (task_name, priority, deadline)
        self.scores = {}  # Dictionary: { "Math": [90, 85], "Science": [78, 72] }

    def add_task(self, task_name, priority, deadline):
        """Add a new study task with validation."""
        if not task_name.strip():
            return "Error: Task name cannot be empty."

        if not isinstance(priority, int) or not (1 <= priority <= 5):
            return "Error: Priority must be an integer between 1 and 5."

        try:
            deadline_obj = datetime.strptime(deadline, "%Y-%m-%d").date()
            if deadline_obj < datetime.today().date():
                return "Error: Deadline cannot be in the past."
        except ValueError:
            return "Error: Deadline must be in YYYY-MM-DD format."

        self.tasks.append((task_name, priority, deadline))
        self.tasks.sort(key=lambda x: (x[1], x[2]))  # Sort tasks
        return "Task added successfully."

    def get_tasks(self):
        """Return the sorted task list."""
        return self.tasks

    def add_score(self, subject, score):
        """Add a score for a subject."""
        if subject not in self.scores:
            self.scores[subject] = []
        self.scores[subject].append(score)

    def get_average_scores(self):
        """Calculate and return the average score for each subject."""
        return {subject: sum(scores) / len(scores) for subject, scores in self.scores.items()}
