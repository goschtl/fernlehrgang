# -*- coding: utf-8 -*-

from cromlech.dawnlight import ViewLookup
from cromlech.dawnlight import view_locator, query_view
from cromlech.configuration.utils import load_zcml
from cromlech.i18n import register_allowed_languages


view_lookup = ViewLookup(view_locator(query_view))


def configuration(global_conf, zcml_file, langs):
    """A factory for the configuration middleware.
    It's usually used to initialize some parameters,
    register components and possibly wrap the requested
    apps.
    """

    # Read the ZCML
    # -------------
    # We make sure it's called only once.
    # There's no builtin safeguard to verify that.
    load_zcml(zcml_file)

    # Register the i18n preferences
    # -----------------------------
    # Needed by the templating system to resolve the
    # translation by retrieving the active language
    # from the request. All this system lives in `cromlech.i18n`.
    allowed = langs.strip().replace(',', ' ').split()
    register_allowed_languages(allowed)

    def app_wrapper(app):
        """The effective middleware. Here, we do not make use
        of the wrapping capabilities, but it can be used to
        add other explicit middlewares.
        """
        return app

    return app_wrapper
