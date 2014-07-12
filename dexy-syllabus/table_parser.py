import pandas as pd
import numpy as np
import tabulate
import jinja2

class_number = '438'
schedule_file = '{}-syllabus.xlsx'.format(class_number)
template_file = '{}-syllabus.jinja'.format(class_number)
markdown_file = '{}-syllabus.md'.format(class_number)

def create_full_table(schedule, columns):

    rdf = schedule[columns]
    rdf = schedule[np.isfinite(schedule['Lecture'])]

    for col in columns:
        if col is not 'Lecture':
            rdf[col] = rdf[col].fillna('')

    tablestr = tabulate.tabulate(rdf[columns].values, headers=columns, tablefmt='pipe')
    #print(tablestr)
    return tablestr

def create_partial_table(schedule, columns):

    rdf = schedule[columns]
    rdf = rdf.dropna()
    tablestr = tabulate.tabulate(rdf[columns].values, headers=columns, tablefmt='pipe')
    #print(tablestr)
    return tablestr

schedule = pd.read_excel(schedule_file, 'schedule', index='Lecture')
course_schedule = create_full_table(schedule, ['Lecture', 'Date', 'Topic'])
project_schedule = create_partial_table(schedule, ['Date', 'Project'])
reading_schedule = create_partial_table(schedule, ['Date', 'Reading'])
homework_schedule = create_partial_table(schedule, ['Date', 'Homework'])

with open('course-schedule.md', 'w') as f:
    f.write(course_schedule)
