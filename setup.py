#!/usr/bin/env python
import os
from distutils.core import setup

import sys

package_dir = {
    'PyDbLite.test':'test'
    }

package_data = {
    'doc':['*.html','*.css','fr/*.html','fr/*.css',
        'en/*.html','en/*.css']
    }

setup(name='PyDbLite',
      version='2.5',
      description='PyDbLite, a fast, pure-Python in-memory database',
      author='Pierre Quentel',
      author_email='pierre.quentel@gmail.com',
      url='http://www.pydblite.net/',
      packages=['PyDbLite','PyDbLite.test'],
      package_dir=package_dir,
      package_data=package_data,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Topic :: Database :: Database Engines/Servers'
          ]
     )

