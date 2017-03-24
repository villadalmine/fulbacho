import logging

def log_message(msg):
    msg = "Fulbacho API: " + msg
    return msg

def log_error(msg):
    logging.error(log_message(msg))
    return log_message(msg)

def check_keys(apitoken):
    if not apitoken:
        msg = 'APITOKEN is needed!'
        log_error(msg)
        raise ValueError(msg)
