from pyramid.view import view_config
from pyramid.response import Response
from od_scraper import od_scraper
import logging

from sqlalchemy.exc import DBAPIError
import pyramid.httpexceptions as exc

from qdhome.models.home import Home


class PopulateView:
    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)

    @view_config(route_name='qdhome_populate')
    def qdhome_populate(self):
        try:
            generator = od_scraper.return_home_generator()
        except BaseException as e:
            self.log.critical(e)
            raise exc.HTTPServerError()

        counter = 1
        for data in generator:
            print(counter)
            counter += 1
            for it in data:
                try:
                    query = self.request.dbsession.query(Home)
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
                    self.request.dbsession.add(new_home)
                    self.request.dbsession.flush()

        return Response('<body><h1>Hello World!</h1></body>', status=200)
