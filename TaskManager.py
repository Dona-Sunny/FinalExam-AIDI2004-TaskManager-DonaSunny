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
        
        def deleteTask(self, task_id):
            """
        Deletes a task by its ID.
        """
        self.tasks = [task for task in self.tasks if task["id"] != task_id]