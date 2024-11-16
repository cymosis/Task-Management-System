
class Task:
    _id_counter = 1

    def __init__(self, title, due_date, description=None):
        self._task_id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.due_date = due_date
        self._description = description if description is None or len(description) <= 15 else None
        self.status = "pending"
        self.flag = None

    def mark_completed(self):
        self.status = "completed"

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if len(value) > 15:
            raise ValueError("Description exceeds 15 characters.")
        self._description = value

    def __str__(self):
        return f"Task ID: {self._task_id}, Title: {self.title}, Due: {self.due_date}, Status: {self.status}"


class PersonalTask(Task):
    def __init__(self, title, due_date, description=None, priority="low"):
        super().__init__(title, due_date, description)
        self.priority = priority

    def is_high_priority(self):
        return self.priority == "high"

    def set_priority(self, priority):
        if priority in ["high", "medium", "low"]:
            self.priority = priority
        else:
            print("Invalid priority value. Use 'high', 'medium', or 'low'.")

    def __str__(self):
        return super().__str__() + f", Priority: {self.priority}"


class WorkTask(Task):
    def __init__(self, title, due_date, description=None, team_members=None):
        super().__init__(title, due_date, description)
        self.team_members = team_members if team_members else []

    def add_team_member(self, member):
        if member:
            self.team_members.append(member)
        else:
            print("Invalid team member name.")

    def __str__(self):
        return super().__str__() + f", Team Members: {', '.join(self.team_members)}"
