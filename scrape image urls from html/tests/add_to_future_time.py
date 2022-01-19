import datetime
import time



print(datetime.datetime.now())
time_diff = 10
time_change = datetime.timedelta(seconds=time_diff)

now = datetime.datetime.now()

target_time = now + time_change

while datetime.datetime.now() < target_time:
    time.sleep(1)
    now = datetime.datetime.now()
    #print(target_time - now)
    #print((now - target_time).seconds)
    #print((target_time - now).seconds)
    if ((target_time - now).seconds) > time_diff :
        break

    elif ((target_time - now).seconds) == time_diff:
        break
    print((target_time - now).seconds)

print("done")