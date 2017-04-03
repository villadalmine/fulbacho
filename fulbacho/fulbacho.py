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
        self.allLeagues = ""
    def setLeaguesAll(self, leaguesAll):
        self.allLeagues = leaguesAll
    def getLeaguesAll(self):
        return self.allLeagues
    def get_url_status(self, query=None):
        base_url = self.server.getUrl()
        if query is None:
            api_query = self.getApiQuery()
            apitoken = self.getApiToken()
            url = (base_url+"&key="+apitoken+api_query)
            status_url = Client.get_url_status(url)
            newreq = requests.get ( url )
            json = newreq.json()
            self.setLeaguesAll(json)
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
            if "*" in key:
                country = key.replace("*", "")
                nameList.append(country)
                idList.append(id)
            else:
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
                reqliga = requests.get ( url )
                urlLeague = reqliga.json()
                countryName = id[item]
                idLeague = item
                leagueAttr = self.getLeaguesAttributes(countryName, idLeague)
                self.leagues.append(FulbachoLiga(urlLeague, countryName, idLeague, year, leagueAttr))
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
            liga = self.leagues[i].getNameLeague()
            country = self.leagues[i].getLeagueCountry()
            name = name + " League: " + liga + " Country: "+ country
            #print (self.leagues[i].getName())
        return name
    def isName(self, name):
        for i in range(self.getQtyLeagues()):
            if self.leagues[i].getCountryName == name:
                return True
            else:
                return False
    def checkName(self, name):
        if self.isName(name) is True:
            return "The Name " + name + " is a valid league"
        else:
            return "The Name " + name + " is not a valid load league"
    def getLeaguesAttributes(self, countryName, idLeague, query=None):
        if countryName == 'am':
            nameCountry = countryName
        else:
            nameCountry = countryName.title()
        attrLeague = dict()
        for item  in range(len(self.getLeaguesAll()['category']['leagues'][nameCountry])):
            if self.getLeaguesAll()['category']['leagues'][nameCountry][item]['id'] ==  idLeague:
                attrLeague['league_id'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['league_id']
                attrLeague['name'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['name']
                attrLeague['total_rounds'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['total_rounds']
                attrLeague['year'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['year']
                attrLeague['continent'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['continent']
                attrLeague['current_round'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['current_round']
                attrLeague['country'] = self.getLeaguesAll()['category']['leagues'][nameCountry][item]['country']
        return attrLeague
    def reloadLeagueData(self):
        for item in range(self.getQtyLeagues()):
            countryName = self.leagues[item].getCountryName()
            idLeague = self.leagues[item].getIdLeague()
            leagueAttr = self.getLeaguesAttributes(countryName, idLeague)
            self.leagues[item].setLeagueAttr(leagueAttr)



class FulbachoLiga(Liga):
    def __init__(self, json=None, countryName=None, idLeague=None,  year=None, leagueAttr=None, matches=None,):
        Liga.__init__(self, json, countryName, idLeague, year, leagueAttr )
    def getCurrentMatches(self):
        return self.getLeagueAttr()['current_rounds']
    def getTotalMatches(self):
        return self.getLeagueAttr()['total_rounds']
    def getNameLeague(self):
        return self.getLeagueAttr()['name']
    def getLeagueCountry(self):
        return self.getLeagueAttr()['country']
        """
       def setAttrOfLeagues(self, query=None):
           base_url = self.server.getUrl()
           if query is None:
               api_query = self.getApiQuery()
           else:
               api_query = query
           apitoken = self.getApiToken()
           url = (base_url+"&key="+apitoken+api_query)
           status_url = Client.get_url_status(url)
           if status_url is True:
               req = requests.get ( url )
               for i in range(len(req.json()["category"]["leagues"]["Argentina"])):
                   req.json()["category"]["leagues"]["Argentina"][0]
               return status_url
           else:
               return "League can not be configured because query api is not ok" + base_url + "token" + api_query
       """
