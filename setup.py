#!/usr/bin/python
#coding=utf-8

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	

config={
	'description': 'PisXw_WebApp',
	'author': 'XuWei',
	'url': 'Url to get it',
	'download_url': 'Where to download it',
	'author_email': 'xwnjnu@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': ['bin/run.py'],
	'name': 'PisXw_WebApp'
}

setup(**config)
