import os


from ..core.handlers import ReverseProxyHandler

prefix = 'person'
url_prefix = '/{}/'.format(prefix)

apis = {
    'library': {
        'title': 'Library API',
        'href': 'http://api.m.ox.ac.uk/library/',
    },
    'contacts': {
        'title': 'Contact Search API',
        'href': 'http://api.m.ox.ac.uk/contact/',
        'path': 'contact',
    },
    'river-status': {
        'title': 'River Status API',
        'href': 'http://api.m.ox.ac.uk/rivers/',
        'path': 'rivers',
    },
    'transport': {
        'title': 'Transport Information API',
        'href': 'http://api.m.ox.ac.uk/transport/',
    },
    'places': {
        'title': 'Places API',
        'href': 'http://api.m.ox.ac.uk/places/',
    },
}

def hook_in(app):
    for name in apis:
        definition = apis[name].copy()
        del definition['href']
        path = definition.pop('path', name)
        app['definitions'][name] = definition

        app.router.add_route('*', '/{path}/{{path:.*}}'.format(path=path),
                             ReverseProxyHandler(app, apis[name]['href']),
                             name='{name}:reverse-proxy'.format(name=name))
        app.router.add_route('*', '/{path}/'.format(path=path),
                             lambda request: None,
                             name='{name}:index'.format(name=name))

