#local
from .connections import Client, Server
from .common import configure
#pip
configparser
# API server
PROTOCOL = 'http'
HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
TEST_HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
VERSION = ''
APIQUERY = '&format=json&req=leagues'
ENVOSVAR =
FILENAMEKEY =
PATHNAMEKEY =


class Fulbacho(Client):
    def __init__(self, test=False, timeout=30):
        server = Server()
        Client.__init__(self, server, timeout)
    def get_url_status(self, query=None):
        base_url = self.server.url
        if query is None:
            api_query = self.apiquery
        else:
            api_query = query
        apitoken = self.apitoken
        url = (base_url+"&key="+apitoken+api_query)
        status_url = Client.get_url_status(url)
        return status_url
    def initialize_config(self):
        config = configure()
        protocol = config['SERVER']['PROTOCOL']
        self.server.protocol = protocol
        host = config['SERVER']['HOST']
        self.server.host = host
        self.server.setUrl()
        version = config['SERVER']['VERSION']
        self.server.version = version
        self.apiquery = config['FULBACHO']['APIQUERY']
        self.apitoken = check_keys()
        """ FALTA CHEQUEAR LA FUNCION DE CHECKKEYS"""
