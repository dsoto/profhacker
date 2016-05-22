import datetime as dt

'''
for class stuff generation, pass start and end dates, class meeting
days, and holidays and a template to get stuff back.

    def generate_stuff(day_start,     # first day of instruction
                       day_end,       # last day of instruction
                       meeting_days,  # class days by isoweekday()
                       holidays,      # holidays as a list of datetimes
                       template)      # string with placeholder for dates

for day to day planning, it would be good to have a command line
application that could give a formatted date range starting today

    > emit_dates -n 30


I could also use enumerate to get the lecture number and this to get the
week number of the semester.

    week=d.isocalendar()[1]-start_date.isocalendar()[1]+1))
'''

# emit dates continuously starting with start_date
def emit_dates(start_date):
    this_date = start_date
    while True:
        yield this_date
        this_date += dt.timedelta(days=1)

# filter dates by holiday and class day
def emit_class_dates(start_date, class_days, holidays):
    for this_date in emit_dates(start_date):
        if this_date in holidays:
            continue
        if this_date.isoweekday() in class_days:
            yield this_date

# generate a list of strings from the class dates
def emit_strings(start_date=dt.date.today(),
                 end_date=None,
                 days=None,
                 holidays=(),
                 template_string='{date:%a %d %b %Y}'):
    for this_date in emit_class_dates(start_date, days, holidays):
        if this_date > end_date:
            break
        yield template_string.format(date=this_date)

# write to file or print to stdout the strings from dates
def write_dates(start_date=dt.date.today(),
                end_date=None,
                days=None,
                holidays=(),
                template_string='{date:%a %d %b %Y}',
                file_out=None):
    if file_out == None:
        for string in emit_strings(start_date, end_date, days, holidays, template_string):
                print(string)
    else:
        with open(file_out, 'w') as f:
            for string in emit_strings(start_date, end_date, days, holidays, template_string):
                f.write(string)
                f.write('\n')

