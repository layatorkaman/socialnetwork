import json
from os import path


def load_with_json(file_name, key=None):
    if path.isfile(file_name):
        with open(f'{file_name}', 'r') as file:
            if key:
                execute = json.load(file)[key]
            else:
                execute = json.load(file)
            return execute
    else:
        return {}


def dump_in_json(file_name, data, key1, key2=None):
    if path.isfile(file_name):
        with open(file_name, 'r') as file:
            data_from_file = json.load(file)

            if key1 in data_from_file.keys() and key2:
                data_from_file[key1].update({key2: data})

            elif (key1 in data_from_file.keys()) and (not key2):
                data_from_file[key1] = data

            elif key1 not in data_from_file.keys() and key2:
                data_from_file[key1] = {key2: data}

            elif key1 not in data_from_file.keys() and (not key2):
                data_from_file.update({key1: data})

        with open(file_name, 'w') as file:
            json.dump(data_from_file, file, indent=4, ensure_ascii=False)

    else:

        if key1 and key2:
            new_data = {key1: {key2: data}}
        elif key1 and not key2:
            new_data = {key1: data}
        elif not key1 and key2:
            print('missing username as key..')

        with open(file_name, 'w') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

        return f'data has been written into {file_name} successfully'
