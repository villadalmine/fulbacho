import logging
import os
import requests

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

def get_url_status(url):
    """Handles api.football-data.org requests"""
    req = requests.get( url )
    if req.status_code == requests.codes.ok:
        if not req.text == "info-not-allowed-request-for-api-account-type":
            if not req.text == "no-version":
                if req.json:
                    print ( "a" )
                else:
                    msg = 'Response is not a Json!'
                    log_error(msg)
                    raise ValueError(msg)
            else:
                msg = 'Response is a no-version!'
                log_error(msg)
                raise ValueError(msg)
        else:
           msg = 'Response is info-not-allowed-request-for-api-account-type'
           log_error(msg)
           raise ValueError(msg)
    else:
        msg = 'Response is not 200 OK!'
        log_error(msg)
        raise ValueError(msg)
