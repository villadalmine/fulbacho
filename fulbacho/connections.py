class Server:
	def __init__(self, protocol, host, version=None ):
		url = '{0:s}://{1:s}'.format(protocol, host)
		if version:
			url = '{0:s}/{1:s}'.format(url, version)

		self.PROTOCOL = protocol
		self.HOST = host
		self.VERSION = version
		self.URL = url



class Client(object):
	def __init__(self, server: Server, timeout=30):
		self.SERVER = server
		self.TIMEOUT = timeout

	def check_api():
		"""Check Server api connections"""
