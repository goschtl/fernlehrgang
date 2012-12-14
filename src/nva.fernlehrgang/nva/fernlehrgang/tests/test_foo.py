import nva.fernlehrgang
from cromlech.browser.testing import TestRequest
from zope.interface import implements
from nva.fernlehrgang.interfaces import ISQLSite
from nva.fernlehrgang.views import SiteIndex
from zope.component import getMultiAdapter
from .testing import configure


class Context(object):
    implements(ISQLSite)
    contents = []


def test_index():
    request = TestRequest()
    context = Context()
    index = SiteIndex(context, request)
    assert index.contents() == []
    assert index.render() == u'<html>\n    <head></head>\n    <body>\n        <h1> KLAUS </h1>\n    </body>\n</html>\n'


def pytest_funcarg__config(request):
    return configure(request, nva.fernlehrgang, 'configure.zcml')


def test_integration(config):
    test_request = TestRequest()
    context = Context()
    index = getMultiAdapter((context, test_request), name=u"index")
    assert index.contents() == []
    assert index.render() == u'<html>\n    <head></head>\n    <body>\n        <h1> KLAUS </h1>\n    </body>\n</html>\n'
