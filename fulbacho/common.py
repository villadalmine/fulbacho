import logging
import os

def log_message(msg):
    msg = "Fulbacho API: " + msg
    return msg

def log_error(msg):
    logging.error(log_message(msg))
    return log_message(msg)

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
