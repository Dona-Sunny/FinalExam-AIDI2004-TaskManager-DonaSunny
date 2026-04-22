# Final Exam AIDI 2004 - Dona Sunny

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, title, priority):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority
        }
        self.tasks.append(task)