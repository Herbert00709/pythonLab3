from pathlib import Path

DAYS = {
    "pn": "poniedziałek",
    "wt": "wtorek",
    "sr": "środa",
    "czw": "czwartek",
    "pt": "piątek",
    "sob": "sobota",
    "nd": "niedziela",
}


def create_day_names_from_range(day_range: str) ->  list[str]:
    first_and_last = day_range.split('-')
    if len(first_and_last) == 1:
        if first_and_last[0] not in DAYS:
            raise ValueError(f"Invalid range: {day_range}")
        return [DAYS[first_and_last[0]]]
    
    elif len(first_and_last) == 2:
        first, last = first_and_last
        
        if first not in DAYS or last not in DAYS:
            raise ValueError(f"Invalid range: {day_range}")
        keys_of_days = list(DAYS.keys())
        i = keys_of_days.index(first)
        j = keys_of_days.index(last)
        if i > j:
            raise ValueError(f"Invalid order in range: {day_range}")

        ans = []
        for k in keys_of_days[i : j + 1]:
            ans.append(DAYS[k])
        return ans
    else:
        raise ValueError(f"Invalid range: {day_range}")

def create_path(months: list[str], day_ranges: list[str], 
                times_of_days: list[str]) -> list[Path]:
    if len(months) != len(day_ranges):
        raise ValueError("Number of day ranges must be equal to number of months.")

    paths = []
    index_of_time_of_day = 0
    for month, dayRange in zip(months, day_ranges):
        day_names = create_day_names_from_range(dayRange)
        for day in day_names:
            if index_of_time_of_day < len(times_of_days):
                time_of_day = times_of_days[index_of_time_of_day]
            else:
                time_of_day = "r"
            if time_of_day not in ("r", "w"):
                raise ValueError(f"Invalid time of day: {time_of_day}")
            
            name_of_time_of_day = 'rano' if time_of_day == "r" else 'wieczorem'

            p = Path(month.capitalize()) / day / name_of_time_of_day

            paths.append(p)
            index_of_time_of_day += 1

    if len(times_of_days) > index_of_time_of_day:
        raise ValueError("Too many times of days.")

    return paths



