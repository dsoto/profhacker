from sys import argv

file_input = 'test.ipynb'
file_input = argv[1]
file_output = 'test_out.ipynb'
file_output = argv[2]

import json

with open(file_input) as f:
    doc = json.loads(f.read())

def is_not_solution(c):
    # for now if solution tag exists assume True
    if 'solution' not in c['metadata']:
        return True
    else:
        return False


new_cells = list(filter(is_not_solution, doc['cells']))
doc['cells'] = new_cells

# delete cells from dictionary with certain metadata
# if 'solution': True exists in metadata, remove from list
with open(file_output, 'w') as f:
    f.write(json.dumps(doc))

