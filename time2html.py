from datetime import datetime
import time

f = open("time.html", "w+")

for i in range(10):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f.write("<p>The time is "  + current_time + "</p>\r")
    print("This is " + str(i) + " time")
    time.sleep(1)

f.close()