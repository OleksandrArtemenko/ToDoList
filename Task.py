from State import State
from Subtask import Subtask


class Task:
    __all_tasks = []

    def __init__(self, title, deadline, description=""):
        for task in Task.__all_tasks:
            if task.__title == title:
                return

        self.__title = title
        self.__deadline = deadline
        self.__description = description
        self.__status = State.get_by_title("New")
        self.__subtasks = []
        Task.__all_tasks.append(self)

    def __repr__(self):
        return (f"Task(title={self.__title}, deadline={self.__deadline}, "
                f"description={self.__description}, status={self.__status}, "
                f"subtasks={self.__subtasks})")

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_deadline(self):
        return self.__deadline

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_subtasks(self):
        return self.__subtasks

    def add_subtask(self, subtask_title, subtask_status=None):
        subtask = Subtask(subtask_title, subtask_status)
        self.__subtasks.append(subtask)

    def read_subtask(self, subtask_title):
        for subtask in self.__subtasks:
            if subtask.title == subtask_title:
                return subtask

    def update_subtask(self, subtask_title, status=None):
        subtask = self.read_subtask(subtask_title)
        if subtask and status:
            subtask.set_status(status)

    def delete_subtask(self, subtask_title):
        subtask = self.read_subtask(subtask_title)
        if subtask:
            self.__subtasks.remove(subtask)

    def mark_subtask_as_complete(self, subtask_title):
        subtask = self.read_subtask(subtask_title)
        if subtask:
            complete_state = State.get_by_title("Complete")
            if complete_state:
                subtask.set_status(complete_state)

    @classmethod
    def get_all_tasks(cls):
        return cls.__all_tasks

    @classmethod
    def get_task_by_title(cls, title):
        for task in cls.__all_tasks:
            if task.get_title() == title:
                return task



if __name__ == "__main__":
    State.initialize_default_states()


