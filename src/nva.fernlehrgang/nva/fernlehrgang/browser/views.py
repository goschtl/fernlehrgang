# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import dolmen.view

from nva.fernlehrgang.interfaces import ISQLSite
from cromlech.webob.response import Response
from dolmen.layout import Layout
from dolmen.view import query_view, make_layout_response
from grokcore.component import name, context
from grokcore.security import require
from js.jqueryui import black_tie
from nva.fernlehrgang.resources import bootstrap
from nva.fernlehrgang.utils import get_template
from zope.interface import Interface


class FLGLayout(Layout):
    context(Interface)

    responseFactory = Response
    template = get_template('layout.pt')

    title = u"Fernlehrgang"

    def __call__(self, content, **extra):
        black_tie.need()
        bootstrap.need()
        return Layout.__call__(self, content, **extra)


class SiteIndex(dolmen.view.View):
    name('index')
    context(Interface)
    require('zope.Public')
    responseFactory = Response
    make_response = make_layout_response

    template = get_template('homepage.pt')

    def contents(self):
        items = []
        for content in self.context.contents:
            view = query_view(self.request, content, name='summary')
            if view is not None:
                view.update()
                items.append(view.render())
        return items
