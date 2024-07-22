import tkinter as tk
from tkinter import simpledialog, messagebox
from ToDo import ToDo
from State import State

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.todo = None
        self.create_initial_screen()

    def create_initial_screen(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Enter ToDo List name:")
        self.label.pack()

        self.todo_list_name_entry = tk.Entry(self.root)
        self.todo_list_name_entry.pack()

        self.create_todo_list_button = tk.Button(self.root, text="Create ToDo List", command=self.create_todo_list)
        self.create_todo_list_button.pack()

        self.load_todo_list_button = tk.Button(self.root, text="Load ToDo List from file", command=self.load_todo_list)
        self.load_todo_list_button.pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_todo_list(self):
        todo_list_name = self.todo_list_name_entry.get()
        if todo_list_name:
            self.todo = ToDo(todo_list_name)
            self.root.title(todo_list_name)
            self.create_task_screen()

    def load_todo_list(self):
        filename = simpledialog.askstring("Input", "Enter filename to load:")
        if filename:
            try:
                self.todo = ToDo.load_from_file(filename)
                self.root.title(self.todo.to_dict()['title'])
                self.create_task_screen()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load ToDo list: {e}")

    def create_task_screen(self):
        self.clear_window()

        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=1)

        self.create_task_button = tk.Button(self.root, text="Create Task", command=self.create_task)
        self.create_task_button.pack()

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.create_subtask_button = tk.Button(self.root, text="Create Subtask", command=self.create_subtask)
        self.create_subtask_button.pack()

        self.update_subtask_button = tk.Button(self.root, text="Update Subtask", command=self.update_subtask)
        self.update_subtask_button.pack()

        self.delete_subtask_button = tk.Button(self.root, text="Delete Subtask", command=self.delete_subtask)
        self.delete_subtask_button.pack()

        self.mark_task_complete_button = tk.Button(self.root, text="Mark Task as Complete", command=self.mark_task_as_complete)
        self.mark_task_complete_button.pack()

        self.mark_subtask_complete_button = tk.Button(self.root, text="Mark Subtask as Complete", command=self.mark_subtask_as_complete)
        self.mark_subtask_complete_button.pack()

        self.save_to_file_button = tk.Button(self.root, text="Save ToDo List to File", command=self.save_todo_list)
        self.save_to_file_button.pack()

        self.display_tasks()

    def display_tasks(self):
        # Clear existing task widgets
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        print(f"Number of widgets after clearing: {len(self.tasks_frame.winfo_children())}")

        if self.todo:
            tasks = self.todo.to_dict()['tasks']
            print(f"Tasks to display: {tasks}")  # Debug print to check the tasks list
            for i, task in enumerate(tasks, start=1):
                task_info = f"{i}. {task['title']} (Deadline: {task['deadline']}, Status: {task['status']})"
                task_label = tk.Label(self.tasks_frame, text=task_info)
                task_label.pack(anchor='w')

                # Display task description
                task_description = tk.Label(self.tasks_frame, text=f"   Description: {task['description']}")
                task_description.pack(anchor='w')

                # Display subtasks
                for j, subtask in enumerate(task['subtasks'], start=1):
                    subtask_info = f"   {i}.{j}. {subtask['title']} (Status: {subtask['status']})"
                    subtask_label = tk.Label(self.tasks_frame, text=subtask_info)
                    subtask_label.pack(anchor='w')

    def create_task(self):
        title = simpledialog.askstring("Input", "Enter task title:")
        deadline = simpledialog.askstring("Input", "Enter task deadline:")
        description = simpledialog.askstring("Input", "Enter task description:")
        if title and deadline:
            self.todo.add_task(title, deadline, description)
            self.display_tasks()  # Refresh the displayed tasks

    def update_task(self):
        title = simpledialog.askstring("Input", "Enter task title to update:")
        if title:
            task = self.todo.read_task(title)
            if task:
                deadline = simpledialog.askstring("Input", "Enter new deadline:", initialvalue=task.get_deadline())
                description = simpledialog.askstring("Input", "Enter new description:", initialvalue=task.get_description())
                status_title = simpledialog.askstring("Input", "Enter new status:", initialvalue=task.get_status().title)
                status = State.get_by_title(status_title) if status_title else None
                self.todo.update_task(title, deadline, description, status)
                self.display_tasks()
            else:
                messagebox.showerror("Error", f"Task '{title}' not found")

    def delete_task(self):
        title = simpledialog.askstring("Input", "Enter task title to delete:")
        if title:
            self.todo.delete_task(title)  # Remove the task from the ToDo list
            self.display_tasks()  # Refresh the displayed tasks

    def create_subtask(self):
        task_title = simpledialog.askstring("Input", "Enter parent task title:")
        if task_title:
            subtask_title = simpledialog.askstring("Input", "Enter subtask title:")
            if subtask_title:
                subtask_status = State.get_by_title("New")  # Default status
                self.todo.add_subtask_to_task(task_title, subtask_title, subtask_status)
                self.display_tasks()  # Refresh the displayed tasks

    def update_subtask(self):
        task_title = simpledialog.askstring("Input", "Enter parent task title:")
        if task_title:
            subtask_title = simpledialog.askstring("Input", "Enter subtask title to update:")
            if subtask_title:
                status_title = simpledialog.askstring("Input", "Enter new status:")
                status = State.get_by_title(status_title) if status_title else None
                self.todo.update_subtask_in_task(task_title, subtask_title, status)
                self.display_tasks()  # Refresh the displayed tasks

    def delete_subtask(self):
        task_title = simpledialog.askstring("Input", "Enter parent task title:")
        if task_title:
            subtask_title = simpledialog.askstring("Input", "Enter subtask title to delete:")
            if subtask_title:
                self.todo.delete_subtask_from_task(task_title, subtask_title)
                self.display_tasks()  # Refresh the displayed tasks

    def mark_subtask_as_complete(self):
        task_title = simpledialog.askstring("Input", "Enter parent task title:")
        if task_title:
            subtask_title = simpledialog.askstring("Input", "Enter subtask title to mark as complete:")
            if subtask_title:
                self.todo.update_subtask_in_task(task_title, subtask_title, State.get_by_title("Complete"))
                self.display_tasks()  # Refresh the displayed tasks

    def mark_task_as_complete(self):
        title = simpledialog.askstring("Input", "Enter task title to mark as complete:")
        if title:
            self.todo.update_task(title, self.todo.read_task(title).get_deadline(), self.todo.read_task(title).get_description(), State.get_by_title("Complete"))
            self.display_tasks()  # Refresh the displayed tasks

    def save_todo_list(self):
        filename = simpledialog.askstring("Input", "Enter filename to save:")
        if filename:
            try:
                self.todo.save_to_file(filename)
                messagebox.showinfo("Success", f"ToDo list saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save ToDo list: {e}")

if __name__ == "__main__":
    State.initialize_default_states()
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
