#http://apiclient.resultados-futbol.com/scripts/api/api.php?key=&tz=America/Buenos_Aires&format=json&lang=es&clang=es&code=ar&req=tables&league=192&group=all&country=ar&year=2017'
import os, requests, json

class Liga:
    def __init__(self, json=None, name=None ):
            self.json = json
            self.name = name
    def getJson(self):
        return self.json
    def setJson(self, json):
        self.json = json
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = nme
    def getLeague(self, name=None):
        """TESTING"""
