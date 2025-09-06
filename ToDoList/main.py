import csv


class Task:
    def __init__(self, titlu, description):
        self.title = titlu
        self.description = description
    def __str__(self):
        return f"{self.title}: {self.description}"

class TaskManager:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_task()
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task {title} added succesfully")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed successfully!")
                return
        print(f"Task '{title}' not found!")
    def display_task(self):
        if not self.tasks:
            print("no tasks available")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def save_task(self):
        with open(self.filename, "w", newline='') as file:
            write = csv.writer(file)
            write.writerow(["Title", "Description"])
            for task in self.tasks:
                write.writerow([task.title, task.description])
        print("Tasks saved")
    def load_task(self):
        try:
            with open(self.filename, "r", newline='') as file:
                reader = csv.reader(file)
                try:
                    next(reader)
                except StopIteration:
                    print("File empty")
                    return
                self.tasks = [Task(row[0], row[1]) for row in reader]
            print("Tasks loaded")
        except FileNotFoundError:
            print("File not found")

def main():
    manager = TaskManager()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == 2:
            title = input("Enter task title: ")
            manager.remove_task(title)
        elif choice == 3:
            manager.display_task()
        elif choice == 4:
            manager.save_task()
        elif choice == 5:
            manager.save_task()
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()