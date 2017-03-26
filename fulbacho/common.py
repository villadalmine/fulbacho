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

"""
def check_keys():
    try:
        apitoken = os.environ['FULBACHO_API_TOKEN']
        return apitoken
    except KeyError:
        home = os.path.expanduser("~")
        config = os.path.join(home, ".env")
        if os.path.exists(config):
            with open(config, "r") as cfile:
                key = cfile.read()
                if key:
                    apitoken = key.replace('\n','')
                    return apitoken
        else:
            msg = 'APITOKEN is needed!'
            log_error(msg)
            raise ValueError(msg)
"""

def configure( directory=None ):
    config = configparser.ConfigParser()
    config['SERVER'] = { 'HOST': 'apiclient.resultados-futbol.com/scripts/api/api.php?', 'PROTOCOL': 'http', 'TEST_HOST': 'apiclient.resultados-futbol.com/scripts/api/api.php?', 'VERSION': ''}
    config['CLIENT'] = { 'TIMEOUT': '' }
    if directory is None:
        cwd = os.getcwd()
        config['FULBACHO'] = { 'APIQUERY': '&format=json&req=leagues', 'ENVOSVAR': 'FULBACHO_API_TOKEN', 'FILENAMEKEY': '.env', 'PATHNAMEKEY': cwd }
        with open(cwd+'/fulbacho.ini', 'w') as configfile:
            config.write(configfile)
    else:
        home = os.path.dirname(directory)
        real_path = "fulbacho.ini"
        abs_file_path = os.path.join(home, real_path)
        config['FULBACHO'] = { 'APIQUERY': '&format=json&req=leagues', 'ENVOSVAR': 'FULBACHO_API_TOKEN', 'FILENAMEKEY': '.env', 'PATHNAMEKEY': directory }
        with open(abs_file_path, 'w') as configfile:
            config.write(configfile)
    return config
