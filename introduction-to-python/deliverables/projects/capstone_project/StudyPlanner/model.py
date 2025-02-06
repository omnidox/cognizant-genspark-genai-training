from datetime import datetime 

# model.py - Study Planner Core Logic (Independent of GUI)
class StudyPlannerModel:
    # def __init__(self):
        # self.tasks = []  # List of (task_name, priority, deadline)
        # self.scores = {}  # Dictionary: { "Math": [90, 85], "Science": [78, 72] }

    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(StudyPlannerModel, cls).__new__(cls)
            cls._instance.tasks = []  # Keeps tasks persistent
            cls._instance.scores = {}  # Keeps scores persistent
        return cls._instance


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
        """Add a score for a subject with validation."""
        if not subject.strip():
            return "Error: Subject name cannot be empty."

        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            return "Error: Score must be a number between 0 and 100."

        if subject not in self.scores:
            self.scores[subject] = []
        self.scores[subject].append(score)

        return f"Score {score} added for {subject}."  # ✅ Always returns a message


    def get_all_scores(self):
        """Retrieve all subjects and their scores."""
        return self.scores  # Returns the dictionary {"Math": [90, 85], "Science": [78, 72]}

    def get_average_scores(self):
        """Calculate and return the average score for each subject."""
        if not self.scores:
            return {}

        return {subject: sum(scores) / len(scores) for subject, scores in self.scores.items()}
