import logging
from model import StudyPlannerModel

class StudyPlannerController:
    def __init__(self):
        self.model = StudyPlannerModel()
        logging.basicConfig(filename="study_planner.log", level=logging.INFO)

    def add_task(self, task_name, priority, deadline):
        """Handles adding a new task after validation."""
        if not task_name or not deadline:
            return "Error: Task name and deadline are required."
        
        try:
            priority = int(priority)
            if not (1 <= priority <= 5):
                return "Error: Priority must be between 1 and 5."
        except ValueError:
            return "Error: Priority must be an integer."

        message = self.model.add_task(task_name, priority, deadline)
        
        # Only log successful additions
        if "Error" not in message:
            logging.info(f"Task Added: {task_name}, Priority: {priority}, Deadline: {deadline}")
        
        return message

    def get_tasks(self):
        """Retrieves the task list."""
        return self.model.get_tasks()

    def add_score(self, subject, score):
        """Handles adding a new score after validation."""
        if not subject.strip():
            return "Error: Subject name cannot be empty."
        
        try:
            score = float(score)  # Accepts both integers and floats
            if not (0 <= score <= 100):
                return "Error: Score must be between 0 and 100."
        except ValueError:
            return "Error: Score must be a valid number."

        message = self.model.add_score(subject, score)

        # Only log successful additions
        if "Error" not in message:
            logging.info(f"Score Added: {subject} - {score}")

        return message
    
    def get_all_scores(self):
        """Retrieve all subjects and their scores."""
        return self.model.get_all_scores()  # ✅ Calls the function from model.py

    def get_average_scores(self):
        """Retrieves the average scores per subject."""
        return self.model.get_average_scores()
