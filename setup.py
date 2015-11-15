#!/usr/bin/env python

import sys
from os.path import join, dirname
from ez_setup import use_setuptools
from setuptools import setup

sys.path.append(join(dirname(__file__), 'src'))
use_setuptools()

DESCRIPTION = """
FlexSeleniumLibrary is a web testing library for Robot Framework
to manipulate Adobe Flex applications.
"""[1:-1]

setup(name         = 'robotframework-flexseleniumlibrary',
      version      = '0.1.0',
      description  = 'Adobe Flex testing library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Toni Lappalainen',
      author_email = '<hirsivaja@users.noreply.github.com>',
      url          = 'https://github.com/hirsivaja/FlexSeleniumLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing testautomation selenium webdriver flex',
      platforms    = 'any',
      install_requires = [
          'selenium >= 2.32.0',
          'robotframework >= 2.6.0'
      ],
      py_modules=['ez_setup'],
      package_dir  = {'' : 'src'},
      packages     = ['FlexSeleniumLibrary','FlexSeleniumLibrary.keywords'],
      include_package_data = True,
      )