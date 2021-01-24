import ntpath
import os


def name_from_path(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def method_select():
    switcher = 0
    while not(switcher == '1' or switcher == '2'):
        switcher = input("Are you: \n[1] Philtering\n[2] Dephiltering\n")

    if switcher == '1':
        return 'philter'
    else:
        return 'dephilter'


def make_directories(data):
    print("Current Dir" + os.getcwd())
    directory = os.getcwd() + "/" + data['SOURCE_DIR']
    try:
        os.mkdir(directory)
    except OSError:
        print("Found Source Directory")
    else:
        print(
            "Made Source Directory. Please populate it with .webms and re-run the script.")

    directory = os.getcwd() + "/" + data['SOURCE_DIR'] + "/processed"
    try:
        os.mkdir(directory)
    except OSError:
        pass
    else:
        pass

    directory = os.getcwd() + "/" + data['FINAL_DIR']
    try:
        os.mkdir(directory)
    except OSError:
        print("Found Destination Directory")
    else:
        print("Made Destination Directory.")

    directory = os.getcwd() + "/" + data['REFACE_DIR']
    try:
        os.mkdir(directory)
    except OSError:
        print("Found Reface Directory")
    else:
        print("Made Reface Directory.")

    directory = os.getcwd() + "/" + data['REFACE_DIR'] + "/processed"
    try:
        os.mkdir(directory)
    except OSError:
        pass
    else:
        pass

    directory = os.getcwd() + "/" + data['DEPHILTERED_DIR']
    try:
        os.mkdir(directory)
    except OSError:
        print("Found DePhiltered Directory")
    else:
        print("Made DePhiltered Directory.")


def get_filenames(folder):
    """Trawls through your videos directory and scrapes all webm files

    Returns:
    file_list (List of Strings): Webm files to process
    """
    file_list = []
    directory = os.getcwd() + "/" + folder

    for filename in os.listdir(directory):
        if filename.endswith(".webm") or filename.endswith(".mp4") or filename.endswith(".m4v") or filename.endswith(".gif"):
            file_list.append(os.path.join(directory, filename))
        else:
            continue
    return file_list
