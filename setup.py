#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """
FlexSeleniumLibrary is a web testing library for Robot Framework
to manipulate Adobe Flex applications. Flex applications bootstrapped
with SeleniumFlexAPI or FlexPilot can be programmatically controlled with
this library.
"""[1:-1]

setup(name             = 'robotframework-flexseleniumlibrary',
      version          = '0.3.0',
      description      = 'Adobe Flex testing library for Robot Framework',
      long_description = DESCRIPTION,
      author           = 'Toni Lappalainen',
      author_email     = '<hirsivaja@users.noreply.github.com>',
      url              = 'https://github.com/hirsivaja/FlexSeleniumLibrary',
      license          = 'Apache License 2.0',
      keywords         = 'robotframework testing testautomation selenium '
                         'webdriver flex FlexPilot SeleniumFlexAPI',
      platforms        = 'any',
      install_requires = ['robotframework-selenium2library >= 1.7.0'],
      package_dir      = {'' : 'src'},
      packages         = ['FlexSeleniumLibrary',
                          'FlexSeleniumLibrary.keywords'],
      include_package_data = True,
      )