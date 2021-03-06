from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
import logging

from sqlalchemy.exc import DBAPIError
import pyramid.httpexceptions as exc

from qdhome.models.m_home import Home
from qdhome.services.s_home import HomeService
from qdhome.models.m_admin import AdminSettings
from qdhome.services.s_admin import AdminSettingsService
from qdhome.forms.f_admin import AdminPanelForm

from qdhome.celery import test_task2


# TODO clean this shit up
class AdminView:
    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)

    @view_config(route_name='qd_admin', match_param='action=edit',
                 renderer='../templates/qd_admin.jinja2')
    def admin_panel(self):
        entry = AdminSettingsService.find_first(self.request)
        form = AdminPanelForm(self.request.POST, entry)

        # I don't know why WTForm doesn't set checkbox as checked, that's why I need to do this manually
        form.should_email.checked = entry.should_email if entry else False;

        if self.request.method == 'POST' and form.validate():
            entry = entry if entry else self.__init_admin_settings()
            form.populate_obj(entry)
            return HTTPFound(location=self.request.route_url('qd_admin', action='edit'))

        return {'form': form, 'action': self.request.matchdict.get('action')}

    @view_config(route_name='qd_admin', match_param='action=clear',
                 renderer='../templates/qd_admin_message.jinja2')
    def admin_clear_db(self):
        if HomeService.clear_db(self.request.dbsession):
            return {"message": "Db Cleared"}
        else:
            return {"message": "Something goes wrong - 500"}

    @view_config(route_name='qd_admin', match_param='action=rebuild',
                 renderer='../templates/qd_admin_message.jinja2')
    def admin_rebuild_db(self):
        result = True # TODO clean this
        test_task2.delay()
        if result:
            return {"message": "Db Rebuilded"}
        else:
            return {"message": "Something goes wrong - 500"}

    def __init_admin_settings(self):
        entry = AdminSettings()
        AdminSettingsService.insert_db(self.request.dbsession, obj=entry)
        return entry
