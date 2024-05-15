class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task index: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "4":
            index = int(input("Enter task index: "))
            todo_list.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
