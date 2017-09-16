from psd import Service, ServiceDiscovery

def __main__():
	servers1 = ['abc.aws.com','abc2.aws.com','abc3.aws.com','abc4.aws.com']
	service1 = Service('abc', servers1)
	servers2 = ['def.aws.com','def2.aws.com','def3.aws.com']
	service2 = Service('def', servers2)

	serviceDiscovery = ServiceDiscovery()
	serviceDiscovery.register(service1)
	serviceDiscovery.register(service2)

	service = serviceDiscovery.get('def')
	print service

if __name__ == '__main__':
	__main__()