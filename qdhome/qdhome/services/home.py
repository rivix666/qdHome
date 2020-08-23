import logging
from qdhome.models.home import Home
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from od_scraper import od_scraper

class HomeService:
    log = logging.getLogger(__name__)

    @classmethod
    def by_id(cls, _id, request):
        try:
            query = request.dbsession.query(Home)
            return query.filter(Home.id == _id).first()
        except DBAPIError as e:
            cls.log.critical(e)
            return None

    @classmethod
    def dict_all_debug(cls, request):
        try:
            query = request.dbsession.query(Home)
        except DBAPIError as e:
            cls.log.critical(e)
            return None
        return query
