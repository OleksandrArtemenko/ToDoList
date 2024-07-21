from Task import Task
from State import State


class TaskService:

    def __init__(self):
        State.initialize_default_states()

    @staticmethod
    def create_task(title, description=""):
        return Task(title, description)

    @staticmethod
    def read_task(title):
        return Task.get_task_by_title(title)

    @staticmethod
    def update_task(title, description="", status=""):
        task_to_update = Task.get_task_by_title(title)
        if task_to_update:
            if description is not None:
                task_to_update.set_description(description)
            if status is not None:
                if State.get_by_title(status):
                    task_to_update.set_status(status)

    @staticmethod
    def delete_task(title):
        task_to_delete = Task.get_task_by_title(title)
        if task_to_delete in Task.get_all_tasks():
            Task.get_all_tasks().remove(task_to_delete)

    @staticmethod
    def add_subtask_to_task(task_title, subtask_title, subtask_description=""):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task in Task.get_all_tasks():
            selected_task.add_subtask(subtask_title, subtask_description)

    @staticmethod
    def read_subtask_from_task(task_title, subtask_title):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task in Task.get_all_tasks():
            selected_task.read_subtask(subtask_title)

    @staticmethod
    def update_subtask_in_task(task_title, subtask_title, description="", status=""):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task in Task.get_all_tasks():
            selected_task.update_subtask(subtask_title, description, status)

    @staticmethod
    def delete_subtask_from_task(task_title, subtask_title):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task in Task.get_all_tasks():
            selected_task.delete_subtask(subtask_title)

