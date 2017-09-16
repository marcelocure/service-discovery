from functools import reduce
from random import randint


class Service(object):
	def __init__(self, name, servers=[]):
		self.servers = servers
		self.name = name

	def include_server(self, server):
		self.servers.append

	def remove_server(self, server):
		self.servers = servers.remove(server)

	def get_smoothest_server(self):
		randomIndex = randint(0, len(self.servers)-1)
		return self.servers[randomIndex]

	def __str__(self):
		return "name: {0}, servers: {1}".format(self.name, str(self.servers))

class ServiceDiscovery(object):
	def __init__(self, services=[]):
		self.services = services

	def register(self, service):
		self.services.append(service)

	def get(self, name):
		service = filter(lambda service: service.name == name, self.services)[0]
		return "{0}/{1}".format(service.get_smoothest_server(), name)

	def __str__(self):
		return reduce(lambda service, acc: service.join(acc), map(str, self.services))
