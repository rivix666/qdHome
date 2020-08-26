from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
import logging

from sqlalchemy.exc import DBAPIError
import pyramid.httpexceptions as exc

from qdhome.models.m_home import Home
from qdhome.services.s_home import HomeService
from qdhome.services.s_admin import AdminSettingsService
from qdhome.forms.f_admin import AdminPanelForm


# TODO clean this shit up
class AdminView:
    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)

    @view_config(route_name='qd_admin', match_param='action=edit',
                 renderer='../templates/qd_admin.jinja2')
    def admin_panel(self):
        entry = AdminSettingsService.find_first(self.request)
        entry = entry if entry else AdminSettingsService.prepare_default(self.request)
        form = AdminPanelForm(self.request.POST, entry)

        if self.request.method == 'POST' and form.validate():
            form.populate_obj(entry)
            return HTTPFound(location=self.request.route_url('qd_admin', action='edit'))

        return {'form': form, 'action': self.request.matchdict.get('action')}

    @view_config(route_name='qd_admin', match_param='action=clear',
                 renderer='../templates/qd_admin_message.jinja2')
    def admin_clear_db(self):
        if HomeService.clear_db(self.request):
            return {"message": "Db Cleared"}
        else:
            return {"message": "Something goes wrong - 500"}

    @view_config(route_name='qd_admin', match_param='action=rebuild',
                 renderer='../templates/qd_admin_message.jinja2')
    def admin_rebuild_db(self):
        if HomeService.rebuild_db(self.request):
            return {"message": "Db Cleared"}
        else:
            return {"message": "Something goes wrong - 500"}
