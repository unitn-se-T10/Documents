#!/usr/bin/env python3

with open("times.log") as f:
    times = f.readlines()

NAMES = {"B": "Bevilacqua", "S": "Sartore", "T": "Tecchio"}


def get_minutes(start, end):
    [sh, sm] = start.split(":")
    [eh, em] = end.split(":")
    minutes = (int(eh) - int(sh)) * 60 + (int(em) - int(sm))
    if minutes < 0:
        minutes += 24 * 60
    return minutes


total_times = {}
for time_entry in times:
    [initials, time_range, _] = time_entry.split("; ")
    [start, end] = time_range.split("-")
    total_time = get_minutes(start, end)
    for char in initials:
        total_times.update({char: total_times.get(char, 0) + total_time})

for key in total_times:
    formatted_time = f"{total_times[key] // 60}h {total_times[key] % 60}m"
    print("{}:\t{}".format(NAMES[key], formatted_time))
