# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from zope.interface import Interface
from zope.schema import TextLine


class ISQLSite(Interface):
    pass


class IUnternehmen(Interface):

    mnr = TextLine(title=u"Mitgliedsnummer")
    title = TextLine(title=u"Titel")
    description = TextLine(title=u"Beschreibung")
