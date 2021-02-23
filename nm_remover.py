# Import Statements
import os
from shutil import rmtree
import sys

# Delete node modules folder in the root directory passed


def node_module_remover(dir):
    count = 0
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            if ('node_modules' in os.path.join(root, name)):
                print('Deleting ' + os.path.join(root, name) + '...')
                rmtree(os.path.join(root, name))
                count += 1

    return count


# Root Directory to delete
dir = sys.argv[1]

# Call node_module_remover
deleted_count = node_module_remover(dir)
print('\n' + str(deleted_count) + ' `node_modules` folders deleted')
