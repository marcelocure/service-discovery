from distutils.core import setup

setup(name='psc',
      version='0.0.1',
      description='Python Service Discovery',
      author='Marcelo Cure',
      author_email='marcelocure@gmail.com',
      url='https://github.com/marcelocure/python-service-discovery/',
      packages=['pml'],
      package_dir={'service-discovery': 'src/service-discovery'},
     )