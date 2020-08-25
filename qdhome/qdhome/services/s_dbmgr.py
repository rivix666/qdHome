import logging
from qdhome.models.m_dbmgr import DbMgrUpdate
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from od_scraper import od_scraper, const

# TODO too long name
class DbMgrUpdateService:
    log = logging.getLogger(__name__)

    @classmethod
    def clear_db(cls, request):
        try:
            request.dbsession.query(DbMgrUpdate).delete()
        except DBAPIError as e:
            cls.log.critical(e)

    @classmethod
    def insert_db(cls, request, data):
        try:
            request.dbsession.add(data)
        except DBAPIError as e:
            cls.log.critical(e)

    @classmethod
    def find_first(cls, request):
        try:
            query = request.dbsession.query(DbMgrUpdate)
            return query.first()
        except DBAPIError as e:
            cls.log.critical(e)
            return None

    @classmethod
    def prepare_default(cls, request):
        entry = DbMgrUpdate()
        entry.first_url = const.MAIN_URL
        entry.range_from = 1
        entry.range_to = 0
        request.dbsession.add(entry)
        return entry

    @classmethod
    def update_by_id(cls, request, _id, data):
        try:
            query = request.dbsession.query(DbMgrUpdate)
            item = query.filter(Home.id == _id).first()
            item.first_url = data.first_url
            item.range_from = data.range_from
            item.range_to = data.range_to
        except DBAPIError as e:
            cls.log.critical(e)