#!/usr/bin/env python3

import time

with open("times.log") as f:
    times = f.readlines()

names = ["Bevilacqua", "Sartore", "Tecchio"]

total_times = {}
total_all = 0
for time_entry in times:
    [name, time_range, _] = time_entry.split("; ")
    [start, end] = time_range.split("-")
    start = time.strptime(start, "%H.%M")
    end = time.strptime(end, "%H.%M")
    total_time = time.mktime(end) - time.mktime(start)
    if name == "Tutti":
        total_all += total_time
    else:
        total_times.update({name: total_times.get(name, 0) + total_time})

for name in names:
    total_times.update({name: total_times.get(name, 0) + total_all})

for key in total_times:
    formatted_time = time.strftime("%H:%M", time.gmtime(total_times[key]))
    print("{}:\t{}".format(key, formatted_time))
