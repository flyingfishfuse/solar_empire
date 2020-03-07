from setuptools import setup

setup(
   name='solar_empire',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=["solar_empire"],  #same as name
   install_requires=['flask' , "flask-sqlalchemy"], #external packages as dependencies
)
