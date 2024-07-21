import json

from Task import Task
from TaskService import TaskService
from ToDo import ToDo
from State import State  # Ensure State is imported if not already in ToDo module


def test_save_and_load():
    # Initialize State
    State.initialize_default_states()

    # Create ToDo instance and add tasks
    # todo = ToDo("My ToDo List")
    # todo.add_task("Task 1", "2024-08-01", "Description for Task 1")
    # todo.add_task("Task 2", "2024-09-01", "Description for Task 2")
    # todo.add_subtask_to_task("Task 1", "Subtask 1", State.get_by_title("In progress"))
    # todo.add_subtask_to_task("Task 2", "Subtask 2", State.get_by_title("Complete"))
    #
    # # Save to file
    filename = "test_todo_list.json"
    # todo.save_to_file(filename)
    # print(f"Saved ToDo list to {filename}")

    # Load from file
    loaded_todo = ToDo.load_from_file(filename)
    print(f"Loaded ToDo list: {loaded_todo.to_dict()}")

if __name__ == "__main__":
    test_save_and_load()

