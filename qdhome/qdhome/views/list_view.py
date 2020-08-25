from pyramid.view import view_config
from pyramid.response import Response
from od_scraper import od_scraper

from sqlalchemy.exc import DBAPIError

from qdhome.services.s_home import HomeService

@view_config(route_name='qd_home', renderer='../templates/qd_index.jinja2')
def qdhome_index(request):
    homes = HomeService.dict_all_debug(request)
    if homes:
        return {"homes": homes}
    else:
        return Response("No data", status=500)



