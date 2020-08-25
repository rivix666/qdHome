from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from od_scraper import od_scraper
import logging

from sqlalchemy.exc import DBAPIError
import pyramid.httpexceptions as exc

from qdhome.models.m_home import Home
from qdhome.services.s_dbmgr import DbMgrUpdateService
from qdhome.forms.f_dbmgr import DbMgrForm


# TODO clean this shit up
class PopulateView:
    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)

    @view_config(route_name='qd_dbmgr', match_param='action=edit',
                 renderer='../templates/qd_updatedb.jinja2')
    def update_db(self):
        entry = DbMgrUpdateService.find_first(self.request)
        entry = entry if entry else DbMgrUpdateService.prepare_default() # TODO check if this will work with empty db
        form = DbMgrForm(self.request.POST, entry)
        if self.request.method == 'POST' and form.validate():
            form.populate_obj(entry)
            return HTTPFound(location=self.request.route_url('qd_dbmgr', action='edit'))

        return {'form': form, 'action': self.request.matchdict.get('action')}

    def debug_refresh_db(self):
        try:
            generator = od_scraper.return_home_generator()
        except BaseException as e:
            log.critical(e)
            raise exc.HTTPServerError()

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

        return Response("Hello World", status=200)
