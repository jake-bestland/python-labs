# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime

now = datetime.now()

print(f"The current date and time is {now}")


dt_str = now.strftime("%m/%d/%Y %H:%M:%S")
print(f"The current date and time is: {dt_str}")