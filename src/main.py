import datetime

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.datetime.now()

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority})"

class ProductivityApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        priority = input("Enter task priority (High/Medium/Low): ")
        new_task = Task(title, priority)
        self.tasks.append(new_task)
        print(f"Task '{title}' added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def complete_task(self):
        self.list_tasks()
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1].complete()
            print(f"Task '{self.tasks[task_num - 1].title}' marked as completed!")
        else:
            print("Invalid task number.")

    def remove_task(self):
        self.list_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(self.tasks):
            removed_task = self.tasks.pop(task_num - 1)
            print(f"Task '{removed_task.title}' removed!")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n--- Productivity App ---")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Complete Task")
            print("4. Remove Task")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.remove_task()
            elif choice == "5":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ProductivityApp()
    app.run()
    
        
