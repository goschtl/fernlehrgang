# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de


from dolmen.content import Model, schema
from nva.fernlehrgang.wsgi_setup.bootstrap import Library
from nva.fernlehrgang.interfaces import IUnternehmen
from sqlalchemy import Column, Integer, String


class Unternehmen(Library, Model):
    """We inherit from Content, since it provides a factory component.
    """
    schema(IUnternehmen)

    __tablename__ = 'unternehmen'

    mnr = Column('id', Integer, primary_key=True)
    title = Column('title', String(50))
    description = Column('synopsis', String(50))

    def __str__(self):
        return str(self.id)
