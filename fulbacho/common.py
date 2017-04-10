import logging
import os
import requests
import configparser

def log_message(msg):
    msg = "Fulbacho API: " + msg
    return msg

def log_error(msg):
    logging.error(log_message(msg))
    return log_message(msg)

def configure( directory=None ):
    config = configparser.ConfigParser()
    config['SERVER'] = { 'HOST': 'apiclient.resultados-futbol.com/scripts/api/api.php?', 'PROTOCOL': 'http', 'TEST_HOST': 'apiclient.resultados-futbol.com/scripts/api/api.php?', 'VERSION': ''}
    config['CLIENT'] = { 'TIMEOUT': '' }
    config['COUNTRIES'] = { 'ARGENTINA': 'Argentina', 'CHILE': 'Chile', 'VENEZUELA': 'am', 'URUGUAY': 'Uruguay', 'ARGENTINA': 'Argentina'}
    config['LEAGUES'] = { 'Argentina': '192', 'Chile': '49', 'am': '113', 'Uruguay': '46', 'Argentina*': '675'}
    if directory is None:
        cwd = os.getcwd()
        config['FULBACHO'] = { 'APIQUERY': '&format=json&req=categories&filter=leagues&country=ar', 'ENVOSVAR': 'FULBACHO_API_TOKEN', 'FILENAMEKEY': '.env', 'PATHNAMEKEY': cwd, 'YEAR': '2017'}
        with open(cwd+'/fulbacho.ini', 'w') as configfile:
            config.write(configfile)
    else:
        home = os.path.dirname(directory)
        real_path = "fulbacho.ini"
        abs_file_path = os.path.join(home, real_path)
        config['FULBACHO'] = { 'APIQUERY': '&format=json&req=categories&filter=leagues&country=ar', 'ENVOSVAR': 'FULBACHO_API_TOKEN', 'FILENAMEKEY': '.env', 'PATHNAMEKEY': directory , 'YEAR': '2017'}
        with open(abs_file_path, 'w') as configfile:
            config.write(configfile)
    return config
#format=json&req=leagues
