from datetime import datetime

cmd = input("Enter command: ")

if cmd == '$time':
    show_time = datetime.now().strftime("%H:%M:%S:%f")
    print(show_time)