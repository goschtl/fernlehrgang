from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='nva.fernlehrgang',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nva'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'cromlech.browser',
          'cromlech.dawnlight',
          'cromlech.security',
          'cromlech.sqlalchemy',
          'cromlech.webob',
          'cromlech.configuration',
          'cromlech.i18n',
          'sqlalchemy',
          'zope.component',
          'zope.event',
          'zope.interface',
          'zope.location',
          'zope.security',
          'dolmen.layout',
          'dolmen.request',
          'dolmen.content',
          'dolmen.view',
          'dolmen.viewlet',
          'dolmen.app.container',
          'dolmen.location',
          'dolmen.breadcrumbs',
          'js.jqueryui',
          'js.bootstrap',
          'BeautifulSoup',
          'infrae.testbrowser',
          'traject',
          # -*- Extra requirements: -*-
      ],
      entry_points={
         'fanstatic.libraries': [
            'nva.fernlehrgang = nva.fernlehrgang.resources:library',
         ],
         'paste.app_factory': [
             'app = nva.fernlehrgang.wsgi_setup.bootstrap:sql_app',
         ],
         'paste.filter_factory': [
             'global_config = nva.fernlehrgang.utils:configuration',
         ],
      }
      )
