import philter as ph
import dephilter as deph
import helpers
import params


def get_config():
    config = params.read_from_file('params.json')
    params.write_to_file('params.json', config)
    print("Config Saved.")
    return config


def main():
    config = get_config()

    helpers.make_directories(config)

    method = helpers.method_select()

    if method == 'philter':
        ph.philter_directory(config)
    elif method == 'dephilter':
        deph.dephilter_directory(config)


if __name__ == "__main__":
    main()
