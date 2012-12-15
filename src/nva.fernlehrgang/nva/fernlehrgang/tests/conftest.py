# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de


import pytest
import nva.fernlehrgang
from nva.fernlehrgang.tests.testing import configure, application


@pytest.fixture(scope="function")
def config(request):
    return configure(request, nva.fernlehrgang, 'configure.zcml')


@pytest.fixture(scope="session")
def app(request):
    return application(request)
