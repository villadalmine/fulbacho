#http://apiclient.resultados-futbol.com/scripts/api/api.php?key=&tz=America/Buenos_Aires&format=json&lang=es&clang=es&code=ar&req=tables&league=192&group=all&country=ar&year=2017'
import os, requests, json
from datetime import datetime, date

class Liga:
    def __init__(self, json=None, countryName=None, idLeague=None, year=None, leagueAttr=None, url=None, matches=None ):
            self.json = json
            self.countryName = countryName
            self.idLeague = idLeague
            self.matches = matches
            self.year = year
            self.leagueAttr = leagueAttr
            self.matchPerDay = url
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
    def getMatches(self):
        return self.matches
    def setMatches(self, matches):
        self.json = matches
    def getIdLeague(self):
        return self.idLeague
    def setIdLeague(self, idLeague):
        self.idLeague = idLeague
    def getLeagueName(self):
        return self.leagueName
    def setLeagueName(self, leagueName):
        self.leagueName = leagueName
    def getLeagueAttr(self):
        return self.leagueAttr
    def setLeagueAttr(self, leagueAttr):
        self.leagueAttr = leagueAttr
    def setUrlMatchPerDay(self):
        url = self.getUrlMatchPerDay()
        hour = self.getToday()
        totalUrl = url+hour
        final = str(totalUrl)
        self.matchPerDay = final
    def getUrlMatchPerDay(self):
        return self.matchPerDay
    def getToday(self):
        return "{:%Y-%m-%d}".format(datetime.now())
    def setmatchPerDay(self, url):
        self.matchPerDay = url
    def getmatchPerDay(self):
        return self.matchPerDay
