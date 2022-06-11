import time

tim = time.localtime()

actual_time = time.strftime("%d %b %y", tim)
print(actual_time)
time.sleep(5)
actual_time = time.strftime("%d %b %y", tim)
print(actual_time)
time.sleep(5)
actual_time = time.strftime("%d %b %y", tim)
print(actual_time)