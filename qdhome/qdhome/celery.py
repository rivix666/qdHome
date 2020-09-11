import os
import transaction
from pyramid.paster import bootstrap
from qdhome.models import get_tm_session
from qdhome.services.s_home import HomeService
from celery import Celery, Task

# from celery.signals import worker_init

# Deprecated - but working
# @worker_init.connect
# def bootstrap_pyramid(sender, **kwargs):
#     import os
#     from pyramid.paster import bootstrap
#     sender.app.settings = bootstrap('development.ini')['registry'].settings
#
#     customize_settings(sender.app.settings)
#
#     engine = sqlalchemy.create_engine('mysql+mysqldb://root:notarealpassword@127.0.0.1/gs?charset=utf8')
#     DBSession.configure(bind=engine)
#     Base.metadata.bind = engine

app = Celery('tasks', broker='localhost')


class DBTask(Task):
    __session = None

    def after_return(self, *args, **kwargs):
        if self.__session is not None:
            self.__session.remove()

    @property
    def session(self):
        if self.__session is None:
            s_factory = bootstrap('development.ini')['registry']['dbsession_factory']
            with transaction.manager:
                self.__session = get_tm_session(s_factory, transaction.manager)

        return self.__session


# TODO clean this, make it abortable
# Check https://docs.celeryproject.org/en/stable/reference/celery.contrib.abortable.html
@app.task(base=DBTask, bind=True)
def test_task2(self):
    url_list = HomeService.get_all_url_list(self.session)
    for index, url in enumerate(url_list):
        print(index)
        HomeService.scrap_url_and_update_db(url, self.session)