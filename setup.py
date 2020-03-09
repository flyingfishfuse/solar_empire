from setuptools import setup
import pip
import datetime

#things_this_app_needs = ['flask' , "flask-sqlalchemy"]

#def import_or_install(package):
#    for each in package:
#        try:
#            __import__(package)
#        except ImportError:
#            pip.main(['install', package])       

#get all the things!
#import_or_install(things_this_app_needs)

setup(
   name='solar_empire',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=["solar_empire"],  #same as name
   install_requires=['flask' , "flask-sqlalchemy"], #external packages as dependencies
)
