from modules import functions
import PySimpleGUI as PySG

label = PySG.Text("Type in a to-do")
input_box = PySG.InputText(tooltip="Enter todo", key="todo")
add_button = PySG.Button("Add")

window = PySG.Window("My To-Do App",
                     layout=[
                         [label],
                         [input_box, add_button]
                     ],
                     font=('Helvetica', 20)
                     )

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case PySG.WIN_CLOSED:
            break

window.close()
