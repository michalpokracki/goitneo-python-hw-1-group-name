from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    result_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year.replace(year=today.year + 1)
            continue

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.strftime("%A")
            work_weekday = "Monday" if weekday in ["Saturday", "Sunday"] else weekday
            result_dict[work_weekday].append(name)

    for day, names in result_dict.items():
        print(f"{day}: {', '.join(names)}")
