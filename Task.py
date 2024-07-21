from State import State


class Task:

    __all_tasks = []

    def __init__(self, title, description=""):

        for task in Task.__all_tasks:
            if task.__title == title:
                return

        self.__title = title
        self.__description = description
        self.__status = State.get_by_title("New")
        self.__subtasks = []
        Task.__all_tasks.append(self)

    def __repr__(self):
        return ("Task: {" + (f"task title: {self.__title}"
                             f"{f"{", description: " + self.__description if self.__description else ""}"}"
                             f"{f", subtasks: {self.__subtasks}" if self.__subtasks else ""}"
                             f"{f", {self.__status}" if self.__status else ""}") + "}")

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status

    def get_subtasks(self):
        return self.__subtasks

    @classmethod
    def get_all_tasks(cls):
        return cls.__all_tasks

    @classmethod
    def get_task_by_title(cls, title):
        for task in cls.__all_tasks:
            if task.get_title() == title:
                return task

    def add_subtask(self, subtask_title, subtask_description=""):
        if Task.get_task_by_title(subtask_title) is None:
            self.__subtasks.append(Task(subtask_title, subtask_description))

    def read_subtask(self, subtask_title):
        subtask = Task.get_task_by_title(subtask_title)
        if subtask is not None and subtask in self.__subtasks:
            return subtask

    def update_subtask(self, subtask_title, description="", status=""):
        subtask = Task.get_task_by_title(subtask_title)

        if subtask is not None and subtask in self.__subtasks:
            if description is not None:
                subtask.set_description(description)
            if status is not None:
                if State.get_by_title(status):
                    subtask.set_status(status)

    def delete_subtask(self, subtask_title):
        subtask = Task.get_task_by_title(subtask_title)
        if subtask is not None and subtask in self.__subtasks:
            self.__subtasks.remove(subtask)


if __name__ == "__main__":
    State.initialize_default_states()
    print(State.all_states)
    task1 = Task("food", "eating")
    task2 = Task("sleep")
    print(task1)
    print(task2)

