# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from cromlech.browser.testing import TestRequest
from nva.fernlehrgang.browser.views import SiteIndex
from nva.fernlehrgang.interfaces import ISQLSite
from zope.component import getMultiAdapter
from zope.interface import implements


class Context(object):
    implements(ISQLSite)
    contents = []


def test_index():
    request = TestRequest()
    context = Context()
    index = SiteIndex(context, request)
    assert index.contents() == []
    assert index.render() == u'<html>\n    <head></head>\n    <body>\n        <h1> KLAUS </h1>\n    </body>\n</html>\n'


def test_integration(config):
    test_request = TestRequest()
    context = Context()
    index = getMultiAdapter((context, test_request), name=u"index")
    assert index.contents() == []
    assert index.render() == u'<html>\n    <head></head>\n    <body>\n        <h1> KLAUS </h1>\n    </body>\n</html>\n'


def test_app(app):
    assert app.site.title == "Traject-SQL Bookshop"


def test_integration(config, app):
    from infrae.testbrowser.browser import Browser
    browser = Browser(app)
    browser.options.handle_errors = False
    browser.open('http://localhost/')
    assert browser.status == "200 OK"
