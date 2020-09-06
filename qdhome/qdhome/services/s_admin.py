import logging
from qdhome.models.m_admin import AdminSettings
from sqlalchemy.exc import DBAPIError


class AdminSettingsService:
    log = logging.getLogger(__name__)

    @classmethod
    def clear_db(cls, request):
        try:
            request.dbsession.query(AdminSettings).delete()
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
            query = request.dbsession.query(AdminSettings)
            return query.first()
        except DBAPIError as e:
            cls.log.critical(e)
            return None
