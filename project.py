import json

def main():
    todo_list = load_from_file("todo_list.json")
    while True:
        command = input("Enter command (add, view, complete, remove, save, quit): ").strip().lower()
        if command == "add":
            item = input("Enter to-do item: ")
            add_item(todo_list, item)
        elif command == "view":
            view_items(todo_list)
        elif command == "complete":
            item = input("Enter completed item: ")
            mark_complete(todo_list, item)
        elif command == "remove":
            item = input("Enter item to remove: ")
            remove_item(todo_list, item)
        elif command == "save":
            save_to_file(todo_list, "todo_list.json")
        elif command == "quit":
            save_to_file(todo_list, "todo_list.json")
            break
        else:
            print("Unknown command")

def add_item(todo_list, item):
    todo_list.append({"item": item, "completed": False})

def view_items(todo_list):
    for idx, todo in enumerate(todo_list):
        status = "done" if todo["completed"] else "not done"
        print(f"{idx + 1}. {todo['item']} [{status}]")

def mark_complete(todo_list, item):
    for todo in todo_list:
        if todo["item"] == item:
            todo["completed"] = True
            break

def remove_item(todo_list, item):
    todo_list[:] = [todo for todo in todo_list if todo["item"] != item]

def save_to_file(todo_list, filename):
    with open(filename, "w") as file:
        json.dump(todo_list, file)

def load_from_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()

