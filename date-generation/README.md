# Date Generation Script

This is a small date templating library to quickly produce lists of
dates and other text for classroom purposes.

The heavy lifting is done by the dateutil library which allows you to
specify days of the week to create lists of dates.

The datetime syntax and formatting is a little cumbersome, but this
saves me tons of tedium when prepping a new semester or schedule.

The user specifies

- start date
- end date
- templating string
- holidays

The code then produces text output with each of the dates.

## Examples

[Examples on NBViewer](http://nbviewer.ipython.org/github/dsoto/profhacker/tree/master/date-generation/)


Internal variables available in template string

- {date:format string} - date
- {num} - enumeration index, useful for number classes or sessions

I use this to make

- markdown slide templates for lecture
- signups for my office hours
- schedule for syllabus

TODO: implement logic to write the week of the semester
