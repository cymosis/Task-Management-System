
import csv
from datetime import datetime

class TaskManager:
    def __init__(self, task_list_file_name="task_list.csv"):
        self.tasks = []
        self.task_list_file_name = task_list_file_name

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self, flag=None):
        for task in self.tasks:
            if flag is None or task.flag == flag:
                print(task)

    def delete_task(self, task_id):
        for task in self.tasks:
            if task._task_id == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted.")
                return
        print(f"Task ID {task_id} not found.")

    def save_task(self):
        with open(self.task_list_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Due Date", "Status", "Description", "Flag"])
            for task in self.tasks:
                writer.writerow([
                    task._task_id, task.title, task.due_date, task.status,
                    task._description, task.flag
                ])

    def load_task(self):
        try:
            with open(self.task_list_file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("Task file not found.")

    def get_pending_tasks(self):
        return list(filter(lambda task: task.status == "pending", self.tasks))

    def get_overdue_tasks(self):
        return [task for task in self.tasks if datetime.strptime(task.due_date, "%Y-%m-%d") < datetime.now()]
