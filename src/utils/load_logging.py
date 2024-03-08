import logging.config
import yaml
import os


def get_logger(module_name):
    # Load config.yml
    with open(f'{os.getcwd()}/config/config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    logger_path = os.getcwd()+config['logger']['path']


    # Load logging.yml
    with open(logger_path, 'r') as logging_file:
        logging_config = yaml.safe_load(logging_file)

    # Configure logging
    logging.config.dictConfig(logging_config)

    # Now you can use logging as usual
    logger = logging.getLogger(module_name)

    return logger