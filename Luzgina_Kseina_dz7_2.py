import os
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)


def create_starter(data):
    for folder, data_ts in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_t in data_ts:
            if isinstance(data_t, dict):
                create_starter(data_t)
            else:
                if not os.path.exists(data_t):
                    if '.' in data_t:
                        with open(data_t, 'w'):
                            pass
    else:
        os.chdir('../')


if __name__ == '__main__':
    create_starter(config)
