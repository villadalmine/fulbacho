#local
from .connections import Client, Server
from .common import check_keys
# API server
PROTOCOL = 'http'
HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
TEST_HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
VERSION = ''


class Fulbacho(Client):

    def __init__(self, test=False, timeout=30):
        server = Server(PROTOCOL, HOST if not test else TEST_HOST, VERSION)
        Client.__init__(self, server, timeout)
        self.apitoken = check_keys()
