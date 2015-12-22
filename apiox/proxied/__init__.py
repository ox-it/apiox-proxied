import asyncio

from apiox.core import API

apis = {
    'library': {
        'title': 'Library API',
        'base': 'http://api.m.ox.ac.uk/library/',
    },
    'contacts': {
        'title': 'Contact Search API',
        'base': 'http://api.m.ox.ac.uk/contact/',
    },
    'river-status': {
        'title': 'River Status API',
        'base': 'http://api.m.ox.ac.uk/rivers/',
    },
    'transport': {
        'title': 'Transport Information API',
        'base': 'http://api.m.ox.ac.uk/transport/',
    },
    'places': {
        'title': 'Places API',
        'base': 'http://api.m.ox.ac.uk/places/',
    },
}

def declare_api(session):
    for api_id, definition in apis.items():
        definition = definition.copy()
        definition.update({
            'id': api_id,
            'paths': [{
                'sourcePath': '(.*)'.format(api_id),
                'targetPath': '{0}',
            }]
        })
        session.merge(API.from_json(definition))
