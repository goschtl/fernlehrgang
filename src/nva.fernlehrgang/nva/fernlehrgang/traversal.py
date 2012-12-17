# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import traject
from .interfaces import ISQLSite
from .models import Unternehmen
from cromlech.sqlalchemy import get_session
from grokcore.component import order, context, Subscription
from dawnlight.interfaces import IConsumer
from zope.interface import implements
from dolmen.location import get_absolute_url
from cromlech.browser import redirect_response
from cromlech.webob import response
from nva.fernlehrgang.wsgi_setup.bootstrap import Site

PATTERNS = traject.Patterns()


def default_component(root, request):
    def factory(**kwargs):
        url = get_absolute_url(root, request)
        return redirect_response(response.Response, url)
    return factory


class TrajectConsumer(Subscription):
    order(700)
    context(ISQLSite)
    implements(IConsumer)

    def __call__(self, request, root, stack):
        left = '/'.join((name for ns, name in reversed(stack)))
        Default = default_component(root, request)
        unconsumed, consumed, obj = PATTERNS.consume(root, left, Default)
        if consumed:
            return True, obj, stack[:-len(consumed)]
        return False, obj, stack


name = "db"
unternehmen_req = "unternehmen/:mnr:int"


def unternehmen_resolve(name):
    def resolver(mnr):
        session = get_session(name)
        return session.query(Unternehmen).get(mnr)
    return resolver


PATTERNS.register(Site, unternehmen_req, unternehmen_resolve(name))
