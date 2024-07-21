from State import State
from Task import Task
from TaskService import TaskService


class ToDo:

    def __init__(self, title):
        self.__title = title
        self.__ts = TaskService()
        self.__tasks = []

    def add_task(self, title, description=""):
        self.__tasks.append(self.ts.create_task(title, description))

    def read_task(self, title):
        if self.__ts.read_task(title) in self.tasks:
            return self.__ts.read_task(title)

    def update_task(self, title, description="", status=""):
        if self.__ts.read_task(title) in self.__tasks:
            self.__ts.update_task(self.__ts.read_task(title), description, status)

    def delete_task(self, title):
        if self.__ts.read_task(title) in self.__tasks:
            self.__ts.delete_task(self.__ts.read_task(title))



