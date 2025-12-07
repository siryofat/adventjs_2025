take_off = "2025*12*25@00|00|00 NP"

from_times = [
    "2025*12*24@23|59|30 NP",
    "2025*12*25@00|00|00 NP",
    "2025*12*25@00|00|12 NP",
]


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    from datetime import datetime

    parse_string = "%Y*%m*%d@%H|%M|%S NP"
    dt_from = datetime.strptime(from_time, parse_string)
    dt_take_off = datetime.strptime(take_off_time, parse_string)
    delta = dt_take_off - dt_from
    return int(delta.total_seconds())


for from_time in from_times:
    print(time_until_take_off(from_time, take_off))
