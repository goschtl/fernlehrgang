import transaction
from .interfaces import ISQLSite
from .utils import view_lookup
from cromlech.dawnlight import DawnlightPublisher
from cromlech.browser import PublicationBeginsEvent, PublicationEndsEvent
from cromlech.security import Interaction
from cromlech.sqlalchemy import SQLAlchemySession, create_and_register_engine
from cromlech.sqlalchemy import get_session
from cromlech.webob import request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from webob.dec import wsgify
from zope.component import getGlobalSiteManager
from zope.component.hooks import setSite
from zope.event import notify
from zope.interface import implements
from zope.location import Location
from zope.security.proxy import removeSecurityProxy
from cromlech.configuration.utils import load_zcml

Library = declarative_base()


class Site(Location):
    implements(ISQLSite)

    title = u"Traject-SQL Bookshop"
    description = u"An application using `Trajact` and SQLAlchemy."

    def __init__(self, name):
        self.name = name

    @property
    def contents(self):
        return None
        #session = get_session(self.name)
        #return session.query(Author).all()

    def getSiteManager(self):
        return getGlobalSiteManager()

    def add(self, item):
        session = get_session(self.name)
        session.add(item)


class TrajectApplication(object):

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine
        self.site = Site(name)
        self.publisher = DawnlightPublisher(view_lookup=view_lookup)

    def add_object(self, obj, session=None):
        if session is None:
            session = get_session(self.name)
        session.add(obj)

    @wsgify(RequestClass=request.Request)
    def __call__(self, request):
        with SQLAlchemySession(self.engine):
            with transaction.manager:
                with Interaction():
                    setSite(self.site)

                    # Publication is about to begin
                    notify(PublicationBeginsEvent(self.site, request))

                    # publish
                    result = self.publisher.publish(
                        request, self.site, handle_errors=True)

                    # Publication ends
                    notify(PublicationEndsEvent(request, result))

                    setSite()
                    return removeSecurityProxy(result)


def sql_app(global_conf, name, url, zcml_file, **kwargs):
    """A factory used to bootstrap the TrajectApplication.
    As the TrajectApplication will use SQL, we use this
    'once and for all' kind of factory to configure the
    SQL connection and inject the demo datas.
    """
    # We register our SQLengine under a given name
    load_zcml(zcml_file)
    engine = create_and_register_engine(url, name)

    # We bind out SQLAlchemy definition to the engine
    engine.bind(Library)

    # We now instanciate the TrajectApplication
    # The name and engine are passed, to be used for the querying.
    app = TrajectApplication(name, engine)

    # We register our Traject patterns.
    # As we have 2 models, we register 2 resolvers.
    #PATTERNS.register(Site, author_req, author_resolve(name))
    #PATTERNS.register(Site, book_req, book_resolve(name))

    # To finish the initialization process, we inject
    # some test data, to start with something concrete.
    try:
        with transaction.manager:
            with SQLAlchemySession(engine):
                Library.metadata.create_all()
                #inject_data(app)
    except IntegrityError:
        # data already exists, skipping.
        pass

    return app
