import os

current_dir = os.getcwd()
cmd = input("Enter command: ")

if cmd == '$pwd':
    print(current_dir)