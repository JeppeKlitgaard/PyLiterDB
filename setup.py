#!/usr/bin/env python
from distutils.core import setup
from PyLiterDB import VERSION

setup(name='PyLiterDB',
      version='.'.join(VERSION),
      description='PyLiterDB, a fast, pure-Python in-memory database',
      author='Jeppe Klitgaard',
      author_email='jeppe@dapj.dk',
      packages=['PyLiterDB'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Topic :: Database :: Database Engines/Servers'
      ])
