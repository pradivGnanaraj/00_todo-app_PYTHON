from modules import functions
import time

now = time.strftime("%b %d, %Y :::Time::  %H:%M:%S ")
print("Current Time :: ")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        # Context Manager
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, items in enumerate(todos):
            items = items.strip('\n') # removing the additional '\n'
            row = f"{index + 1}-{items}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed cd from the list"
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("***** Invalid Input ******")
exit("Good Bye!")
