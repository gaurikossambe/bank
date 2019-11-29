###     Random values
import random
import time
import datetime


# get a random value between 0 & 1
rnd_value = random.random()
print(rnd_value)

rnd_int = random.randint(100, 1001)
print(rnd_int)

rnd_int_list = [random.randint(1, 1001) for i in range(1, 11)]
print(rnd_int_list)


# 1st Jan 1970 (seconds)
print("Current time: ", time.time())
print("Local time: ", time.localtime(time.time()))
print("Formatted time: ", time.asctime(time.localtime(time.time())))


# Using datetime module
print(datetime.time(6, 35, 34))
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

print(datetime.date.today())
print(datetime.date.today().timetuple())

d1 = datetime.date(2017, 3, 2)
print(d1)
d2 = d1.replace(month=4)
delta = d2-d1
print(delta)
print(type(delta))
print(delta.days)
