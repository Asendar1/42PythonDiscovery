import time
import datetime


time_since_epoch = time.time()
current_datetime = time.strftime("%b %d %Y")

print(f"Seconds since epoch: {time_since_epoch} or {time_since_epoch:.2e} in scientific notation")
print(current_datetime)
