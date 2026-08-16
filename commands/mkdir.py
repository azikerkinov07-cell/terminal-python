import os

current_dir = os.getcwd()
cmd = input("Enter command: ")

if cmd.startswith("$mkdir "):
    dir_name = cmd[7:].strip()
    new_dir_path = os.path.join(current_dir, dir_name)

    try:
        os.makedirs(new_dir_path)
        print(f"Directory '{dir_name}' created.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")