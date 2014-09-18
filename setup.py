#!/usr/bin/env python

from distutils.core import setup

import multipay

setup(name='Django Multipay',
      version='0.0.1',
      description='Integrate multiple django payment apps',
      author='Benjamin Rosnick',
      author_email='benrxv@gmail.com',
      url='https://github.com/benrxv/django-multipay',
      packages=['multipay',],
     )
