from datetime import *

day = str(date.today())
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

print(day, current_time)
print(type(day))
print(type(current_time))