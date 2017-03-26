#local
from .connections import Client, Server
from .common import configure, log_message, log_error
#pip
import configparser
import os
# API server



class Fulbacho(Client):
    def __init__(self, test=False, timeout=30):
        server = Server()
        Client.__init__(self, server, timeout)
    def get_url_status(self, query=None):
        base_url = self.server.getUrl()
        if query is None:
            api_query = self.getApiQuery()
        else:
            api_query = query
        apitoken = self.getApiToken()
        url = (base_url+"&key="+apitoken+api_query)
        status_url = Client.get_url_status(url)
        return status_url
    def initialize_config(self):
        config = configure()
        protocol = config['SERVER']['PROTOCOL']
        self.server.setProtocol(protocol)
        host = config['SERVER']['HOST']
        self.server.setHost(host)
        self.server.setUrl()
        version = config['SERVER']['VERSION']
        self.server.setVersion(version)
        query = config['FULBACHO']['APIQUERY']
        self.setApiQuery(query)
        envOsVar =  config['FULBACHO']['ENVOSVAR']
        fileNameKey = config['FULBACHO']['FILENAMEKEY']
        pathNameKey  = config['FULBACHO']['PATHNAMEKEY']
        result = Client.check_keys(envOsVar, fileNameKey, pathNameKey)
        if result is True:
            apitoken = Client.config_keys(envOsVar, fileNameKey, pathNameKey)
            self.setApiToken(apitoken)
            initilization = self.get_url_status()
            if initilization is True:
                message = log_message ("The API is working")
                return message
        else:
            msg = ("Key is not present")
            log_error(msg)
            raise ValueError(msg)
