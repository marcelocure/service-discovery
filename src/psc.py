
class Service(object):
	def __init__(self, servers, name):
		self.servers = servers
		self.name = name

	def include_server(self, server):
		self.servers.append

	def remove_server(self, server):
		self.servers = servers.remove(server)

class ServiceDiscovery(object):
	def __init__(self, config):
		self.config = config

	def register(self, service):
		self.services.append(service)

	def get_service(self, name):
		service = services.filter(service -> service.name == name, services)
		print service.servers

def __main__():
	pass
