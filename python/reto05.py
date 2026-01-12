def time_until_take_off(from_time: str, take_off_time: str) -> int:
    from datetime import datetime

    parse_string = "%Y*%m*%d@%H|%M|%S NP"
    dt_from = datetime.strptime(from_time, parse_string)
    dt_take_off = datetime.strptime(take_off_time, parse_string)
    delta = dt_take_off - dt_from
    return int(delta.total_seconds())
