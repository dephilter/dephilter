import json


def read_from_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
    except:
        print("Config doesn't exist")
        return read_from_user()

    if is_valid(data):
        print('All variables found in config.')
        return data
    else:
        print("Malformed Config")
        return read_from_user()


def read_from_user():
    print("Enter the following variables. If left blank, defaults are used.")
    data = {}
    data['SOURCE_DIR'] = input("Enter video source directory name \n")
    if not data['SOURCE_DIR']:
        data['SOURCE_DIR'] = 'videos'

    data['FINAL_DIR'] = input("Enter the philtered image directory name \n")
    if not data['FINAL_DIR']:
        data['FINAL_DIR'] = "philtered"

    data['REFACE_DIR'] = input(
        "Enter your reface directory.\n")
    if not data['REFACE_DIR']:
        data['REFACE_DIR'] = "Reface"

    data['DEPHILTERED_DIR'] = input(
        "Enter your de-philtered video directory \n")
    if not data['DEPHILTERED_DIR']:
        data['DEPHILTERED_DIR'] = "dephiltered"

    data['TARGET_FPS'] = input(
        "Enter your gif target FPS\n")
    if not data['TARGET_FPS']:
        data['TARGET_FPS'] = 16
    data['TARGET_FPS'] = int(data["TARGET_FPS"])

    data['MAX_SIZE'] = input(
        "Enter your resolution. Don't go over 600.\n")
    if not data['MAX_SIZE']:
        data['MAX_SIZE'] = 450
    data['MAX_SIZE'] = int(data['MAX_SIZE'])

    data['INITIAL_FRAME'] = 0
    data['FRAME_INTERVAL'] = 10
    data['GRID_TYPE'] = 'grids//hue.png'

    print(data)
    return data


def write_to_file(filepath, config):
    with open(filepath, 'w') as outfile:
        json.dump(config, outfile)


def is_valid(data):
    is_valid = 'SOURCE_DIR' in data and 'FINAL_DIR' in data and 'REFACE_DIR' in data and 'DEPHILTERED_DIR' in data and 'TARGET_FPS' in data and 'INITIAL_FRAME' in data and 'FRAME_INTERVAL' in data and 'GRID_TYPE' in data and 'MAX_SIZE' in data
    print(is_valid)
    return is_valid
