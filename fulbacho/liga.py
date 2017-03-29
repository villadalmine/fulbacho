#http://apiclient.resultados-futbol.com/scripts/api/api.php?key=&tz=America/Buenos_Aires&format=json&lang=es&clang=es&code=ar&req=tables&league=192&group=all&country=ar&year=2017'
import os, requests, json

class Liga:
    def __init__(self, json=None, countryName=None, idLeague=None, year=None, matches=None ):
            self.json = json
            self.countryName = countryName
            self.idLeague = idLeague
            self.matches = matches
            self.year = year
            self.leagueName = ""
    def getJson(self):
        return self.json
    def setJson(self, json):
        self.json = json
    def getCountryName(self):
        return self.countryName
    def setCountryName(self, countryName):
        self.countryName = countryName
    def getLeague(self, name=None):
        """TESTING"""
    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year
    def getmatches(self):
        return self.matches
    def setmatches(self, matches):
        self.json = matches
    def getidLeague(self):
        return self.idLeague
    def setIdLeague(self, idLeague):
        self.idLeague = idLeague
