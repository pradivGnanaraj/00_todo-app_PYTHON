import time

from modules import functions
import PySimpleGUI as PySG

PySG.theme("Black")

clock = PySG.Text('', key='clock')
label = PySG.Text("Type in a to-do")
input_box = PySG.InputText(tooltip="Enter todo", key="todo")
add_button = PySG.Button("Add")
list_box = PySG.Listbox(values=functions.get_todos(),
                        key='todos',
                        enable_events=True,
                        size=[45, 10]
                        )
edit_button = PySG.Button("Edit")
complete_button = PySG.Button("Complete")
exit_button = PySG.Button("Exit")

window = PySG.Window("My To-Do App",
                     layout=[
                         [clock],
                         [label],
                         [input_box, add_button],
                         [list_box, edit_button, complete_button],
                         [exit_button]
                     ],
                     font=('Helvetica', 20)
                     )

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y :::Time::  %H:%M:%S ")

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySG.popup("Please select an item first", font=("Helvetica", 20))

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos()
                window['todos'].update(values=todos)
                window['todo'].update(values='')
            except IndexError:
                PySG.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":
            break

        case PySG.WIN_CLOSED:
            break


window.close()
