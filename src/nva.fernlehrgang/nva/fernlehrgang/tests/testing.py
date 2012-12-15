import os
from zope.testing.cleanup import cleanUp
from zope.configuration import xmlconfig, config
from zope.component.hooks import setHooks


def application(request):
    from nva.fernlehrgang.bootstrap import sql_app
    return sql_app({}, 'testDB', 'sqlite:////Users/christian/work/flgn/fernlehrgang/var/test.db')




def configure(request, module, zcml):
    request.addfinalizer(cleanUp)
    return setup_config(module, zcml)


def setup_config(package, zcml_file):
    zcml_file = os.path.join(os.path.dirname(package.__file__),
                             zcml_file)
    setHooks()
    context = config.ConfigurationMachine()
    xmlconfig.registerCommonDirectives(context)

    return xmlconfig.file(zcml_file,
                          package=package,
                          context=context, execute=True)
