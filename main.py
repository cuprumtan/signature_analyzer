import os
import re
import yaml

import file_searching
import signature_searching


def load_config():
    # load config file
    with open('config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    # check parameters
    #test_dir:
    if not os.path.isdir(config.get('test_dir')):
        print("Error while loading configuration file. Check test_dir value.")
        exit(1)
    # search_dir:
    if not os.path.isdir(config.get('search_dir')):
        print("Error while loading configuration file. Check search_dir value.")
        exit(1)
    # signature_file:
    if str(config.get('signature_file')).lower() != 'random':
        if not os.path.isfile(config.get('signature_file')):
            print("Error while loading configuration file. Check signature_file value.")
            exit(1)
    # signature_size:
    if not (32 <= config.get('signature_size') <= 256):
        print("Error while loading configuration file. Check signature_size value.")
        exit(1)
    # log_file:
    if not os.path.isdir(re.search(r'^(.*[\\\/])', config.get('log_file')).group(0)):
        print("Error while loading configuration file. Check log_file value.")
        exit(1)
    return config


def load_bigrams(file):
    bigrams_dict = {}
    lines = open(file, 'r').readlines()
    for line in lines:
        line_list = line.split()
        bigrams_dict[(int(line_list[0])).to_bytes(2, byteorder='big')] = float(line_list[1])
    return bigrams_dict


if __name__ == "__main__":
    config = load_config()
    bigrams_dict = load_bigrams('bigrams.txt')
    signature = signature_searching.get_signature(bigrams_dict,
                                                  config['signature_file'],
                                                  config['signature_size'],
                                                  config['test_dir'],
                                                  config['log_file'])
    print('\nSignature: ' + str(signature))
    file_searching.search_virus(signature, config['signature_file'], config['search_dir'], config['log_file'])
