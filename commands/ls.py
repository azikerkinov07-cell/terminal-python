import subprocess
import os

current_dir = os.path.expanduser("~")
cmd = input("Enter command: ")

if cmd == "$ls":
    subprocess.run(["ls"], cwd=current_dir)

elif cmd == "$ls -la":
    subprocess.run(["ls", "-la"], cwd=current_dir)

else:
    print("Invalid command. Use $ls or $ls -la.")