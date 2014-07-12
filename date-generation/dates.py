from dateutil import *
from dateutil.rrule import *
import datetime as dt

# this is a generator that outputs days in the range that are not
# holidays
def get_class_dates(first_day, last_day, class_days, holidays):
    dates = list(rrule(DAILY,
                       byweekday=class_days,
                       dtstart=first_day,
                       until=last_day))
    for d in dates:
        if d not in holidays:
            yield d

# templates dates from get_class_dates function
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

# continuously emit dates that are in class days but are not holidays
def emit_class_dates(refdate, class_days, holidays):
    while True:
        if refdate not in holidays and refdate.isoweekday() in class_days:
            yield refdate
        refdate += dt.timedelta(days=1)

# API
# send in a start date, end date, weekdays, holidays, and format string
# get back a text list of rendered dates
# text string optional and get isoformat dates?
# holidays optional
# weekdays optional

def print_dates(start_date=None,
                end_date=None,
                weekdays=range(7),
                holidays=(),
                template_string='{date:%a %d %b %Y}'):
    # is there a better way to do this?
    if start_date == None:
        start_date = dt.date.today()
    if end_date == None:
        end_date = start_date + dt.timedelta(days=7)
    for i, d in enumerate(emit_class_dates(start_date, weekdays,
                                           holidays), start=1):
        if d > end_date:
            break
        print(template_string.format(i=i, date=d,
                                     week=d.isocalendar()[1]-start_date.isocalendar()[1]+1))


# TODO create command line interface dates.py -n numdays -f format

if __name__=='__main__':
    print_dates(dt.date.today())
