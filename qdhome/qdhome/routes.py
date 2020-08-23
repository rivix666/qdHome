def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('qdhome_index', '/')
    config.add_route('qdhome_populate', '/populate_db')
