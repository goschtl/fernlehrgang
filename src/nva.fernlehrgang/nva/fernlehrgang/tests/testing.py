import os
from zope.testing.cleanup import cleanUp
from zope.configuration import xmlconfig, config
from zope.component.hooks import setHooks
from zope.testing.cleanup import cleanUp


def configure(request, module, zcml):
    def setup_function():
        return setup_config(module, zcml)

    return request.cached_setup(setup=setup_function,
                                teardown=teardown_config,
                                scope='function')


def setup_config(package, zcml_file):
    zcml_file = os.path.join(os.path.dirname(package.__file__),
                             zcml_file)
    setHooks()
    context = config.ConfigurationMachine()
    xmlconfig.registerCommonDirectives(context)

    return xmlconfig.file(zcml_file,
                          package=package,
                          context=context, execute=True)


def teardown_config(config):
    cleanUp()
