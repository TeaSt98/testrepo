
import yaml

def get_config():

    with open(r'src/config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    return config