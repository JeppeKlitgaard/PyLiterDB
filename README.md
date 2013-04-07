PyLiterDB
=========

A light pure-python database, that lives in memory, but can be saved to disk. It also does not use SQL syntax, but a more pythonic approach

I forked this from [PyDbLite](http://www.pydblite.net/en/PyDbLite.html), and made, what I think is, improvements.

PyDbLite
========
PyDbLite: [link](http://www.pydblite.net/en/PyDbLite.html)

Differences:
* Removed MySQL and SQLite3 backends, it now only uses the pure-python backend, I did this because I thought there were enough SQL-normalizers on pypi.
* PEP8 compliant. Quite contrary to the origional PyDbLite, this project is made compliant with the standard python guidelines.
* Updated. It has been slightly updated here and there, nothing big.

Dependencies:
============
* None! (Other than python.)

Installation
============
It features a simple setup script, `setup.py`, if you don't know how to use setup.py scripts please see: http://docs.python.org/2/install/

Credits:
========
* Pierre Quentel, the author of PyDbLite, from which this project came. He did the vast majority of the code.
* Jeppe Klitgaard, the author of this fork, PyLiterDB. I really didn't do all that much. All credit is Pierre's.

Docs
====
WORK_IN_PROGRESS
