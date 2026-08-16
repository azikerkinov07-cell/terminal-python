from datetime import datetime

cmd = input("Enter command: ")

if cmd == '$date':
    show_date = datetime.now().strftime("%d.%m.%Y")
    print(show_date)