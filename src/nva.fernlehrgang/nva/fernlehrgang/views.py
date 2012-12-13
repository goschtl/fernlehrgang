# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import os
import dolmen.view

from .interfaces import ISQLSite
from cromlech.webob.response import Response
from dolmen.layout import Layout
from dolmen.template import TALTemplate
from dolmen.view import query_view, make_layout_response
from grokcore.component import name, context
from grokcore.security import require
from js.jqueryui import black_tie
from .resources import bootstrap
from zope.interface import Interface


TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')


def get_template(filename):
    return TALTemplate(os.path.join(TEMPLATES_DIR, filename))


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
    context(ISQLSite)
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
