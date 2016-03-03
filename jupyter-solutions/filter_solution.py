import nbformat
from sys import argv

# TODO: if name main stuff for usage and stderr

file_input = argv[1]

with open(file_input, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)


# slides of type slide are white listed
def is_assigned(c):
    if hasattr(c.metadata, 'slideshow'):
        if c.metadata.slideshow.slide_type == 'slide':
            return True
        else:
            return False
    else:
        return False


new_cells = list(filter(is_assigned, nb['cells']))
nb['cells'] = new_cells
print(nbformat.writes(nb))

