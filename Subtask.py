from State import State


class Subtask:
    def __init__(self, title, status=None):
        self.title = title
        self.status = status if status else State.get_by_title("New")

    def __repr__(self):
        return f"Subtask(title={self.title}, status={self.status})"

    def set_status(self, status):
        self.status = status