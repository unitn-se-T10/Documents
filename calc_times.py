#!/usr/bin/env python3

import time

with open("times.log") as f:
    times = f.readlines()

names = {"B": "Bevilacqua", "S": "Sartore", "T": "Tecchio"}

total_times = {}
for time_entry in times:
    [initials, time_range, _] = time_entry.split("; ")
    [start, end] = time_range.split("-")
    start = time.strptime(start, "%H.%M")
    end = time.strptime(end, "%H.%M")
    total_time = time.mktime(end) - time.mktime(start)
    for char in initials:
        total_times.update({char: total_times.get(char, 0) + total_time})

for key in total_times:
    formatted_time = time.strftime("%H:%M", time.gmtime(total_times[key]))
    print("{}:\t{}".format(names[key], formatted_time))
