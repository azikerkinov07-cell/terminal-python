from datetime import datetime

cmd = input("Enter command: ")

if cmd == '$time&date':
    show_time_date = datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    print(show_time_date)