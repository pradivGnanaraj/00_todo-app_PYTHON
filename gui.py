from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button]]
                   )
window.read()
print("Hello") # gets printed in the console once the application is closed.
window.close()



