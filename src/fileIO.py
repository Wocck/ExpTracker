import json


def json_write(data, path):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('You do not have permission to write to this file')
    except IsADirectoryError:
        print('This is a directory')
    except ValueError:
        print('Invalid data type')


def json_read(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('You do not have permission to write to this file')
    except IsADirectoryError:
        print('This is a directory')
    except ValueError:
        print('Invalid data type')
