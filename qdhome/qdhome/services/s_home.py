import logging
from qdhome.models.m_home import Home
from qdhome.services.s_admin import AdminSettingsService
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from od_scraper import od_scraper, const

class HomeService:
    log = logging.getLogger(__name__)

    @classmethod
    def clear_db(cls, request):
        try:
            request.dbsession.query(Home).delete()
        except DBAPIError as e:
            cls.log.critical(e)
            return False
        else:
            return True

    @classmethod
    def rebuild_db(cls, request):
        try:
            query = AdminSettingsService.find_first(request)
            url = query.first_url if query else const.MAIN_URL
            generator = od_scraper.return_home_generator(url)
        except BaseException as e:
            cls.log.critical(e)
            return False

        # TODO add another thread
        counter = 1
        for data in generator:
            print(counter)
            counter += 1
            for it in data:
                try:
                    query = request.dbsession.query(Home)
                    found = query.filter(Home.desc_url == it.desc_url).first()
                except DBAPIError:
                    return Response(e, content_type='text/plain', status=500)

                if not found:
                    new_home = Home(title=it.title
                                    , price=it.price
                                    , rooms=it.rooms
                                    , area=it.area
                                    , m_price=it.m_price
                                    , district=it.district
                                    , desc_url=it.desc_url)
                    request.dbsession.add(new_home)
                    request.dbsession.flush()

        return True

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
