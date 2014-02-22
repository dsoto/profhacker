from dateutil import *
from dateutil.rrule import *
import datetime as dt

def get_class_dates(first_day, last_day, class_days, holidays):
    dates = list(rrule(DAILY,
                       byweekday=class_days,
                       dtstart=first_day,
                       until=last_day))
    for d in dates:
        if d not in holidays:
            yield d

def output_text(first_day,
                last_day,
                class_days,
                holidays,
                template_string):
    for i, d in enumerate(get_class_dates(first_day,
                                          last_day,
                                          class_days,
                                          holidays), start=1):
        print(template_string.format(num=i, date=d))
