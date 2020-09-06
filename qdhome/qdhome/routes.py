import time
from pyramid.static import QueryStringConstantCacheBuster

def includeme(config):
    # Static views
    config.add_static_view('images', 'static/images', cache_max_age=3600)
    config.add_cache_buster('static/images', QueryStringConstantCacheBuster(str(int(time.time()))))

    config.add_static_view('css', 'static/css', cache_max_age=3600)
    config.add_cache_buster('static/css', QueryStringConstantCacheBuster(str(int(time.time()))))

    config.add_static_view('js', 'static/js', cache_max_age=3600)
    config.add_cache_buster('static/js', QueryStringConstantCacheBuster(str(int(time.time()))))

    # Views
    config.add_route('qd_home', '/')
    config.add_route('qd_admin', '/admin/{action}')
