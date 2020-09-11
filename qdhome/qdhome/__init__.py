from pyramid.config import Configurator
from sqlalchemy import engine_from_config


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # global_confg will return ini used to configure the app
        # config.configure_celery(global_config['__file__'])
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
