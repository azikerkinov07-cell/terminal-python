import os

current_dir = os.getcwd()
cmd = input("Enter command: ")

if cmd.startswith("$cd "):
    path = cmd[4:].strip()

    if path == "..":
        current_dir = os.path.dirname(current_dir)
    elif path == "~":
        current_dir = os.path.expanduser("~")
    
    else:
        new_path = os.path.abspath(os.path.join(current_dir, path))

        if os.path.isdir(new_path):
            current_dir = new_path
        else:
            print(f"Directory '{path}' not found.")