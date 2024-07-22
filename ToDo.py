import json

from State import State
from Task import Task
from TaskService import TaskService


class ToDo:
    def __init__(self, title):
        self.__title = title
        self.__ts = TaskService()
        self.__tasks = []

    def add_task(self, title, deadline, description=""):
        task = self.__ts.create_task(title, deadline, description)
        self.__tasks.append(task)
        return task

    def read_task(self, title):
        return self.__ts.read_task(title)

    def update_task(self, title, deadline=None, description=None, status=None):
        self.__ts.update_task(title, deadline, description, status)

    def delete_task(self, title):
        task_to_delete = self.__ts.read_task(title)
        if task_to_delete:
            self.__tasks.remove(task_to_delete)  # Remove from internal list
            Task.get_all_tasks().remove(task_to_delete)

    def add_subtask_to_task(self, task_title, subtask_title, subtask_status=None):
        self.__ts.add_subtask_to_task(task_title, subtask_title, subtask_status)

    def read_subtask_from_task(self, task_title, subtask_title):
        return self.__ts.read_subtask_from_task(task_title, subtask_title)

    def update_subtask_in_task(self, task_title, subtask_title, status=None):
        self.__ts.update_subtask_in_task(task_title, subtask_title, status)

    def delete_subtask_from_task(self, task_title, subtask_title):
        self.__ts.delete_subtask_from_task(task_title, subtask_title)

    def save_to_file(self, filename):
        data = {'title': self.__title, 'tasks': [self.__task_to_dict(task) for task in self.__tasks]}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        # Initialize the ToDo instance
        todo = ToDo(data['title'])

        # Create tasks and add them to the ToDo instance
        for task_data in data['tasks']:
            task = todo.add_task(task_data['title'], task_data['deadline'], task_data['description'])

            # Add subtasks to the task
            for subtask_data in task_data['subtasks']:
                subtask_status = State.get_by_title(subtask_data['status'])
                task.add_subtask(subtask_data['title'], subtask_status)

        return todo

    def to_dict(self):
        return {'title': self.__title, 'tasks': [self.__task_to_dict(task) for task in self.__tasks]}

    def __task_to_dict(self, task):
        return {
            'title': task.get_title(),
            'deadline': task.get_deadline(),
            'description': task.get_description(),
            'status': task.get_status().title if task.get_status() else None,
            'subtasks': [{'title': subtask.title, 'status': subtask.status.title} for subtask in task.get_subtasks()]
        }
