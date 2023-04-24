## UZDUOTYS:
## Pirma:

from zoneinfo import available_timezones

america_time_zones = []

for tz in available_timezones():
    if "America" in tz:
        america_time_zones.append(tz)

for time_zone in america_time_zones:
    print(time_zone)