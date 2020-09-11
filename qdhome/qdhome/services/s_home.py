import logging
from qdhome.models.m_home import Home
from qdhome.services.s_admin import AdminSettingsService
from sqlalchemy.exc import DBAPIError
from od_scraper import od_scraper, const


class HomeService:
    log = logging.getLogger(__name__)

    @classmethod
    def clear_db(cls, dbsession):
        try:
            dbsession.query(Home).delete()
        except DBAPIError as e:
            cls.log.critical(e)
            return False
        else:
            return True

    @classmethod
    def get_all_url_list(cls, dbsession):
        try:
            query = AdminSettingsService.find_first(dbsession)
            url = query.first_url if query else const.MAIN_URL
            return od_scraper.return_home_pages_list(url)
        except BaseException as e:
            cls.log.critical(e)
            return None

    @classmethod
    def get_all_url_generator(cls, dbsession):
        try:
            query = AdminSettingsService.find_first(dbsession)
            url = query.first_url if query else const.MAIN_URL
            return od_scraper.return_home_generator(url)
        except BaseException as e:
            cls.log.critical(e)
            return None

    @classmethod
    def scrap_url_and_update_db(cls, url, dbsession):
        data = od_scraper.return_page_home_data(url)
        for it in data:
            try:
                found = dbsession.query(Home).filter(Home.desc_url == it.desc_url).first()
            except DBAPIError as e:
                cls.log.critical(e)
                return

            if not found:
                new_home = Home(title=it.title
                                , price=it.price
                                , rooms=it.rooms
                                , area=it.area
                                , m_price=it.m_price
                                , district=it.district
                                , desc_url=it.desc_url)
                dbsession.add(new_home)
                dbsession.flush()  # TODO probably unnecessary

    @classmethod
    def by_id(cls, _id, dbsession):
        try:
            query = dbsession.query(Home)
            return query.filter(Home.id == _id).first()
        except DBAPIError as e:
            cls.log.critical(e)
            return None

    @classmethod
    def dict_all_debug(cls, dbsession):
        try:
            query = dbsession.query(Home)
        except DBAPIError as e:
            cls.log.critical(e)
            return None
        return query
