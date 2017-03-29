#local
from .connections import Client, Server
from .liga import Liga
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
        id_league = config['FULBACHO']['PATHNAMEKEY']
        year_league = config['FULBACHO']['YEAR']
        result = Client.check_keys(envOsVar, fileNameKey, pathNameKey)
        idList = []
        nameList = []
        for key in config['LEAGUES']:
            for otra in config['LEAGUES'][key]:
                id = config['LEAGUES'][key]
            nameList.append(key)
            idList.append(id)
        idAndName = {}
        n = 0
        for i in idList:
            idAndName[i] = nameList[n]
            n = n + 1
        if result is True:
            apitoken = Client.config_keys(envOsVar, fileNameKey, pathNameKey)
            self.setApiToken(apitoken)
            initilization = self.get_url_status()
            initialization_league = self.addLiga(idAndName, year_league)
            if initilization is True and initialization_league is True:
                message = log_message ("The API test is working and all Leagues was added")
                return message
        else:
            msg = ("Key is not present")
            log_error(msg)
            raise ValueError(msg)
    def addLiga(self, id, year):
        """The query is static because it is the same for all leagues"""
        for item in id:
            query = "&tz=America/Buenos_Aires&format=json&lang=es&clang=es&code=ar&req=tables&league="+str(item)+"&group=all&country=ar&year="+year
            urlStatus = self.get_url_status(query)
            if urlStatus is True:
                url = self.getCustomUrl(query)
                req = requests.get ( url )
                urlLeague = req.json()
                name = id[item]
                self.leagues.append(FulbachoLiga(urlLeague, name))
        return True
    def getCustomUrl(self, query):
        base_url = self.server.getUrl()
        apitoken = self.getApiToken()
        url = (base_url+"&key="+apitoken+query)
        return url
    def initialize_leagues(self):
        """Inicializar las ligas con sus equipos"""
    def getQtyLeagues(self):
        return len(self.leagues)
    def getListOfLeagues(self):
        name = ""
        for i in range(self.getQtyLeagues()):
            name = name + " " + self.leagues[i].getName()
            #print (self.leagues[i].getName())
        return name
    def isName(self, name):
        for i in range(self.getQtyLeagues()):
            if self.leagues[i].getName() == name:
                return True
            else:
                return False
    def checkName(self, name):
        if self.isName(name) is True:
            return "The Name " + name + " is a valid league"
        else:
            return "The Name " + name + " is not a valid load league"


class FulbachoLiga(Liga):
    def __init__(self, json=None, name=None ):
        Liga.__init__(self, json, name)
    def getLeague(self, name=None):
        """TESTING"""
