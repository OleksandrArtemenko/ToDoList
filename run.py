from TaskService import TaskService
from ToDo import ToDo


def test_task_management():
    # Initialize TaskService
    ts = TaskService()

    # Test creating tasks
    print("Testing Task Creation")
    task1 = ts.create_task("Task 1", "2024-08-01", "Description for Task 1")
    task2 = ts.create_task("Task 2", "2024-09-01", "Description for Task 2")
    print(f"Created: {task1}")

    # Test reading tasks
    print("\nTesting Task Reading")
    task = ts.read_task("Task 1")
    print(f"Read: {task}")

    # Test updating tasks
    print("\nTesting Task Update")
    ts.update_task("Task 1", description="Updated description for Task 1", status="In progress")
    updated_task = ts.read_task("Task 1")
    print(f"Updated: {updated_task}")

    # Test marking a task as complete
    print("\nTesting Mark Task as Complete")
    ts.update_task("Task 1", status="Complete")
    completed_task = ts.read_task("Task 1")
    print(f"Completed: {completed_task}")

    # Test adding subtasks
    print("\nTesting Add Subtasks")
    ts.add_subtask_to_task("Task 2", "Subtask 1")
    subtask = ts.read_task("Task 2").read_subtask("Subtask 1")
    print(f"Added Subtask: {subtask}")

    # Test updating subtasks
    print("\nTesting Update Subtask")
    ts.update_subtask_in_task("Task 2", "Subtask 1", status="In progress")
    updated_subtask = ts.read_task("Task 2").read_subtask("Subtask 1")
    print(f"Updated Subtask: {updated_subtask}")

    # Test deleting subtasks
    print("\nTesting Delete Subtask")
    ts.delete_subtask_from_task("Task 2", "Subtask 1")
    deleted_subtask = ts.read_task("Task 2").read_subtask("Subtask 1")
    print(f"Deleted Subtask: {deleted_subtask}")  # Should be None

    # Test deleting tasks
    print("\nTesting Delete Task")
    ts.delete_task("Task 1")
    deleted_task = ts.read_task("Task 1")
    print(f"Deleted Task: {deleted_task}")  # Should be None

    # Test saving to and loading from a file
    print("\nTesting Save and Load")
    todo = ToDo("My ToDo List")
    todo.add_task("Task 3", "2024-10-01")
    todo.add_task("Task 4", "2024-11-01")

    # Save to file
    todo.save_to_file("todo_list.json")

    # Load from file
    loaded_todo = ToDo.load_from_file("todo_list.json")
    print(f"Loaded ToDo: {loaded_todo.to_dict()}")

if __name__ == "__main__":
    test_task_management()
