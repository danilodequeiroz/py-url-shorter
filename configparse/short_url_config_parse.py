import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, '../config.ini')
config_parse = configparser.ConfigParser()
config_parse.read(filenames=config_path)

database_user = config_parse['database'].get('user')
database_password = config_parse['database'].get('password')
database_host = config_parse['database'].get('host')
database_port = config_parse['database'].getint('port')
sqids_alphabet = config_parse['sqids'].get('alphabet')