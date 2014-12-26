This directory can generate an output syllabus from a syllabus template
and an XLSX spreadsheet file containing the schedule.  Since I often
change things during the semester and want to regenerate the syllabus
based on those changes, I created this workflow.

For better or worse, a spreadsheet is a natural choice for class
organization where each row is a class period or week in chronological
order.  The table_parser.py script converts the spreadsheet into
markdown files that can be used by the template file.
