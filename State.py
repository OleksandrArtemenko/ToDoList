class State:
    all_states = []

    def __init__(self, title):
        for state in State.all_states:
            if state.title == title:
                return
        self.title = title
        State.all_states.append(self)

    def __repr__(self):
        return f"status: {self.title}"

    def __eq__(self, other):
        return self.title == other.title


    @staticmethod
    def get_by_title(title):
        for state in State.all_states:
            if state.title == title:
                return state

    @classmethod
    def get_all_states(cls):
        return cls.all_states

    @staticmethod
    def initialize_default_states():
        new_state = State("New")
        in_progress_state = State("In progress")
        done_state = State("Done")


if __name__ == "__main__":
    State.initialize_default_states()

    print(State.get_all_states())
    done_state2 = State("Done")
    print(State.get_all_states())
