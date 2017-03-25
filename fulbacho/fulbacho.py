#local
from .connections import Client, Server
from .common import check_keys, get_url_status
# API server
PROTOCOL = 'http'
HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
TEST_HOST = 'apiclient.resultados-futbol.com/scripts/api/api.php?'
VERSION = ''


class Fulbacho(Client):

    def __init__(self, test=False, timeout=30):
        server = Server(PROTOCOL, HOST if not test else TEST_HOST, VERSION)
        Client.__init__(self, server, timeout)
        apitoken = check_keys()
        base_url = server.URL
        url = (base_url+"&key="+apitoken+"&format=json&req=leagues")
        get_url_status(url)

""" DEFINIR BIEN LOS ATRIBUTOS QUE LLEVA LA CLASE Fulbacho
DADO QUE TIENE UN SERVER, UN CLIENTE
EL SERVER TIENE LA API QUE VA A USAR
EL CLIENTE FULBACHO, REDEFINE SUS PROPIOS METODOS PORQUE USA
METODOS DEFAULT DEL OBJETO CLIENTE, PERO AL USAR LA API DE resultados-futbol
HAY QUE DEFINIR LOS ATRIBUTOS QUE USARA; QUE SON PROPIOS DE EL
"""
