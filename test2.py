from State import State
from TaskService import TaskService


def test_task_management():
    # Initialize TaskService
    ts = TaskService()

    # Test creating tasks
    print("Testing Task Creation")
    task1 = ts.create_task("Task 1", "2024-08-01", "Description for Task 1")
    task2 = ts.create_task("Task 2", "2024-09-01", "Description for Task 2")
    ts.add_subtask_to_task("Task 1", "Subtask 1", State.get_by_title("New"))
    ts.add_subtask_to_task("Task 2", "Subtask 2", State.get_by_title("New"))
    print(f"Created: {task1}")

    # Test marking a subtask as complete
    print("\nTesting Mark Subtask as Complete")
    ts.mark_subtask_as_complete("Task 1", "Subtask 1")
    subtask = ts.read_subtask_from_task("Task 1", "Subtask 1")
    print(f"Subtask after marking complete: {subtask}")

if __name__ == "__main__":
    test_task_management()