FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    This function is used as a content manager.
    Returns a text file and return the list of to-do item(s)
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    This function is used to write data to the file
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__cli__":
    print("Hello")
    print(get_todos())
