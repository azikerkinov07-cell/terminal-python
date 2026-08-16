import os
import subprocess

current_dir = os.path.expanduser("~")
cmd = input("Enter command: ")

if cmd.startswith("$cp "):
    parts = cmd[4:].strip().split()

    if len(parts) != 2:
        print("Invalid command. Use $cp <source> <destination>.")
    else:
        source, destination = parts
        source_path = os.path.join(current_dir, source)
        destination_path = os.path.join(current_dir, destination)

        try:
            if os.path.isdir(source_path):
                subprocess.run(["cp", "-r", source_path, destination_path], check=True)
            else:
                subprocess.run(["cp", source_path, destination_path], check=True)

            print(f"Copied '{source}' to '{destination}'.")

        except FileNotFoundError:
            print(f"File or directory '{source}' not found.")
        except subprocess.CalledProcessError:
            print(f"Error copying '{source}'.")