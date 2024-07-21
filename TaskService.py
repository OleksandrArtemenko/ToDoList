from Task import Task
from State import State


class TaskService:

    def __init__(self):
        State.initialize_default_states()

    @staticmethod
    def create_task(title, deadline, description=""):
        return Task(title, deadline, description)

    @staticmethod
    def read_task(title):
        return Task.get_task_by_title(title)

    @staticmethod
    def update_task(title, deadline=None, description=None, status=None):
        task_to_update = Task.get_task_by_title(title)
        if task_to_update:
            if deadline:
                task_to_update.set_deadline(deadline)
            if description:
                task_to_update.set_description(description)
            if status:
                task_to_update.set_status(status)

    @staticmethod
    def delete_task(title):
        task_to_delete = Task.get_task_by_title(title)
        if task_to_delete:
            Task.get_all_tasks().remove(task_to_delete)

    @staticmethod
    def add_subtask_to_task(task_title, subtask_title, subtask_status=None):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task:
            selected_task.add_subtask(subtask_title, subtask_status)

    @staticmethod
    def read_subtask_from_task(task_title, subtask_title):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task:
            return selected_task.read_subtask(subtask_title)

    @staticmethod
    def update_subtask_in_task(task_title, subtask_title, status=None):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task:
            selected_task.update_subtask(subtask_title, status)

    @staticmethod
    def delete_subtask_from_task(task_title, subtask_title):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task:
            selected_task.delete_subtask(subtask_title)

    @staticmethod
    def mark_task_as_complete(title):
        task_to_mark = Task.get_task_by_title(title)
        if task_to_mark:
            complete_state = State.get_by_title("Complete")
            if complete_state:
                task_to_mark.set_status(complete_state)


    @staticmethod
    def mark_subtask_as_complete(task_title, subtask_title):
        selected_task = Task.get_task_by_title(task_title)
        if selected_task:
            selected_task.mark_subtask_as_complete(subtask_title)
