from cromlech.browser.testing import TestRequest
from zope.interface import implements
from nva.fernlehrgang.interfaces import ISQLSite
from nva.fernlehrgang.views import SiteIndex


class Context(object):
    implements(ISQLSite)
    contents = []


def test_index():
    request = TestRequest()
    context = Context()
    index = SiteIndex(context, request)
    assert index.contents() == []
    assert index.render() == u'<html>\n    <head></head>\n    <body>\n        <h1> KLAUS </h1>\n    </body>\n</html>\n'
