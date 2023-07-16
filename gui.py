from modules import functions
import PySimpleGUI as PySG

label = PySG.Text("Type in a to-do")
input_box = PySG.InputText(tooltip="Enter todo")
add_button = PySG.Button("Add")

window = PySG.Window("My To-Do App",
                     layout=[
                         [label],
                         [input_box, add_button]
                     ]
                     )

window.read()
window.close()
