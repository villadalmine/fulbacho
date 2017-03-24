#local
from .connections import Client, Server
from .common import check_keys
# API server
PROTOCOL = 'http'
HOST = 'http://apiclient.resultados-futbol.com/scripts/api/api.php?'
TEST_HOST = 'http://apiclient.resultados-futbol.com/scripts/api/api.php?'
VERSION = 'none'


class Fulbacho(Client):

    def __init__(self, apitoken=False, test=False, timeout=30):
        server = Server(PROTOCOL, HOST if not test else TEST_HOST, VERSION)
        Client.__init__(self, server, timeout)
        check_keys(apitoken)
        self.apitoken = str(apitoken)
