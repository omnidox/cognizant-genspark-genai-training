import logging
from model import StudyPlannerModel

class StudyPlannerController:
    def __init__(self):
        self.model = StudyPlannerModel()
        logging.basicConfig(filename="study_planner.log", level=logging.INFO)

    def add_task(self, task_name, priority, deadline):
        if not task_name or not deadline:
            return "Error: Task name and deadline are required."
        if not isinstance(priority, int) or priority < 1 or priority > 5:
            return "Error: Priority must be between 1 and 5."

        self.model.add_task(task_name, priority, deadline)
        logging.info(f"Task Added: {task_name}, Priority: {priority}, Deadline: {deadline}")
        return "Task added successfully."

    def get_tasks(self):
        return self.model.get_tasks()

    def add_score(self, subject, score):
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            return "Error: Score must be a number between 0 and 100."

        self.model.add_score(subject, score)
        logging.info(f"Score Added: {subject} - {score}")
        return "Score added successfully."

    def get_average_scores(self):
        return self.model.get_average_scores()
