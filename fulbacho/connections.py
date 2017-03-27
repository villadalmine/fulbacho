from .common import log_message, log_error
import os, requests
class Server:
	def __init__(self, protocol=None, host=None, version=None ):
		if protocol is None and host is None:
			url = '{0:s}://{1:s}'.format('http', 'www.test.com')
		else:
			url = '{0:s}://{1:s}'.format(protocol, host)
		if version:
			url = '{0:s}/{1:s}'.format(url, version)
		self.protocol = protocol
		self.host = host
		self.version = version
		self.url = url
	def setUrl(self):
		protocol = self.protocol
		host = self.host
		url = '{0:s}://{1:s}'.format(protocol, host)
		self.url = url
	def getUrl(self):
		return self.url
	def setHost(self, host):
		self.host = host
	def getHost(self):
		return self.host
	def setProtocol(self, protocol):
		self.protocol = protocol
	def getProtocol(self):
		return self.protocol
	def setVersion(self, version):
		self.version = version
	def getVersion(self):
		return self.version


class Client(object):
	def __init__(self, server: Server, timeout=30):
		self.server = server
		self.timeout = timeout
		self.apiquery = ''
		self.apitoken = ''
		self.leagues = []
	def get_url_status(url):
		"""Handles api.football-data.org requests"""
		try:
			requests.get( url )
		except requests.exceptions.ConnectionError as e:
				msg = ("Response is not an url! " + req.text )
				log_error(msg)
				raise ValueError(msg)
		req = requests.get ( url )
		if req.status_code == requests.codes.ok:
			try:
				req.json()
			except ValueError:
					msg = ("Response is not a Json! " + req.text )
					log_error(msg)
					raise ValueError(msg)
			return True
		else:
			msg = ("Response is not 200 OK!" + req.text )
			log_error(msg)
			raise ValueError(msg)
	def check_keys(envOsVar=None, fileNameKey=None, pathNameKey=None):
		if envOsVar is not None or (fileNameKey is not None and pathNameKey is not None):
			return True
		else:
			return False
	def config_keys(envOsVar=None, fileNameKey=None, pathNameKey=None):
	    try:
	        apitoken = os.environ[envOsVar]
	        return apitoken
	    except KeyError:
	        home = os.path.expanduser(pathNameKey)
	        config = os.path.join(home, fileNameKey)
	        if os.path.exists(config):
	            with open(config, "r") as cfile:
	                key = cfile.read()
	                if key:
	                    apitoken = key.replace('\n','')
	                    return apitoken
	        else:
	            msg = ('APITOKEN is needed! in the correct place, you need it here ' + config)
	            log_error(msg)
	            raise ValueError(msg)
	def setApiQuery(self, query):
		self.apiquery = query
	def getApiQuery(self):
		return self.apiquery
	def setApiToken(self, apitoken):
		self.apitoken = apitoken
	def getApiToken(self):
		return self.apitoken

#	def reloadConfig(pathFileName=None, fileName=None):
#		config = configparser.ConfigParser()
#		if pathFileName is None and fileName is None:
				#cwd = os.getcwd()
#				real_path = "fulbacho.ini"
#				abs_file_path = os.path.join(cwd, real_path)
#			if config.read(abs_file_path) != []:
#				"""PENSAR COMO HACER QUE RELEA LA CONFIG"""
#				return True """
