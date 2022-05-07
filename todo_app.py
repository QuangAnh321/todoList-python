# Feature
# 1. Print out all todos
# 2. add a todo
# 3. Update a todo
# 4. Remove a todo

todos = []

while True:
    print("Welcome to Todo App")
    print("0. Exit")
    print("1. View All todos")
    print("2. Add a todo")
    print("3. Update an existing todo")
    print("4. Remove an existing todo")
    user_choice = int(input("How can i help you ? "))

    if user_choice == 0:
        print("See you later!")
        break
    elif user_choice == 1:
        print("Thing(s) that you need to do: ")
        if len(todos) == 0:
            print("Nothing!")
        else:
            for index, todo in enumerate(todos):
                print(f"{index + 1}) {todo}")
    elif user_choice == 2:
        new_todo = input("What do you need to do ? ")
        todos.append(new_todo)
        print("New todo Added successfully")
    elif user_choice == 3:
        todo_to_update_index = int(input("Enter the index of the todo that you want to update: "))
        # Todo: Add Try catch here, for now assume input index exist
        # new_todo.index(todo_to_update_index)
        updated_todo = input("Enter new todo content: ")
        todos[todo_to_update_index - 1] = updated_todo
        print(f"Todo {todo_to_update_index} updated successfully")
    elif user_choice == 4:
        todo_to_remove_index = int(input("Enter the index of the todo that you want to remove: "))
        # Todo: Add Try catch here, for now assume input index exist
        # new_todo.index(todo_to_update_index)
        del todos[todo_to_remove_index - 1]
        print(f"Todo {todo_to_remove_index} remove successfully")
    else:
        print(f"Your choice: {user_choice} is invalid, please try again")

