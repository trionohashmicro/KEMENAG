# -*- encoding: UTF-8 -*-

{
    'name': 'Project Event',
    'version': '10.1.0',
    'author': 'Laxicon Solution',
    'sequence': 10,
    'category': 'event',
    'website': "www.laxicon.in",
    'license': 'LGPL-3',
    'support': 'info@laxicon.com',
    'description': """set project as a event.
    """,
    'depends': ['event', 'project'],
    'data': [
        'views/project_view_interit.xml',
        'views/event_view.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
