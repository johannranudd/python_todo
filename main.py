todos: list[str] = ["milk", "bread", "eggs"]

def show_todos():
    print("======TODOS=======")
    if not todos:
        print("No todos yet.")
        print("=====END=====")
        return


    for i, todo in enumerate(todos, start=1):
        print(f"{i}: {todo}")
        
    print("=====END=====")
        
        
        

def add_todo():
    task = input("New todo: ")
    todos.append(task)
    print("Added.")
    



def edit_todo():
    index = select_todo()
    
    if index is None:
        return
    
    task = input("Change todo to: ")
    todos[index] = task
    print("Updated.")

    
    
def remove_todo():
    index = select_todo()
    
    if index is None:
        return
    
    removed = todos.pop(index)
    print(f"Removed: {removed}")

    
def select_todo() -> int | None:
    if not todos:
        show_todos()
        return None
    
    show_todos()
    print("Select a todo:")

    try:
        index = int(input("> ")) - 1

        if 0 <= index < len(todos):
            return index

    except ValueError:
        pass

    print("Invalid todo number.")
    return None


while True:
    print("\nTodo App")
    print("1. Show todo")
    print("2. Add todo")
    print("3. Edit todo")
    print("4. Remove todo")
    print("9. Quit")

    choice = input("> ")
    
    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        edit_todo()
    elif choice == "4":
        remove_todo()
    elif choice == "9":
        break
    else:
        print("Invalid choice.")


