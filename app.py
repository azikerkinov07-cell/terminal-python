name = input("Enter your name: ")
comp_name = input("Enter your computer name: ")
print("Enter $help to see existing commands.")

from datetime import datetime
import os
import subprocess

current_dir = os.path.expanduser("~")

while True:
    cmd = input(f"{name}@{comp_name}{current_dir}$ ")

    if cmd == '$help':
        print("$help - show commands")
        print("$time - show the time")
        print("$date - show the date")
        print("$time&date - show the time and date")
        print("$cd - change to the directory")
        print("$mkdir - create the directory")
        print("$pwd - show the current directory")
        print("$ls - show directory contents")
        print("$cp - copy the file/directory")
        print("$rm - delete file/directory")
        print("$exit - exit the program")

    elif cmd == '$time':
        show_time = datetime.now().strftime("%H:%M:%S:%f")
        print(show_time)

    elif cmd == '$date':
        show_date = datetime.now().strftime("%d.%m.%Y")
        print(show_date)

    elif cmd == '$time&date':
        show_time_date = datetime.now().strftime("%H:%M:%S %d.%m.%Y")
        print(show_time_date)

    elif cmd.startswith("$cd "):
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

    elif cmd.startswith("$mkdir "):
        dir_name = cmd[7:].strip()
        new_dir_path = os.path.join(current_dir, dir_name)

        try:
            os.makedirs(new_dir_path)
            print(f"Directory '{dir_name}' created.")
        except FileExistsError:
            print(f"Directory '{dir_name}' already exists.")
        except Exception as e:
            print(f"Error creating directory: {e}")

    elif cmd.startswith("$pwd"):
        print(current_dir)

    elif cmd.startswith("$ls"):
        try:
            if cmd == "$ls":
                contents = os.listdir(current_dir)
            elif cmd == "$ls -la":
                contents = os.listdir(current_dir)
                contents = [f for f in contents if not f.startswith('.')] + [f for f in contents if f.startswith('.')]
            else:
                print("Invalid command. Use $ls")
                continue

            for item in contents:
                print(item)
        except Exception as e:
            print(f"Error listing directory contents: {e}")

    elif cmd.startswith("$cp "):
        parts = cmd[4:].strip().split()
        if len(parts) != 2:
            print("Invalid command. Use $cp <source> <destination>.")
            continue

        source, destination = parts
        source_path = os.path.join(current_dir, source)
        destination_path = os.path.join(current_dir, destination)

        try:
            if os.path.isdir(source_path):
                subprocess.run(["cp", "-r", source_path, destination_path])
            else:
                subprocess.run(["cp", source_path, destination_path])
            print(f"Copied '{source}' to '{destination}'.")
        except Exception as e:
            print(f"Error copying: {e}")

    elif cmd.startswith("$rm "):
        target = cmd[4:].strip()
        target_path = os.path.join(current_dir, target)

        try:
            if os.path.isdir(target_path):
                subprocess.run(["rm", "-r", target_path])
            else:
                subprocess.run(["rm", target_path])
            print(f"Deleted '{target}'.")
        except Exception as e:
            print(f"Error deleting: {e}")

    elif cmd == '$exit':
        print("Exiting the program.")
        break