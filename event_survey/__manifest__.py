# -*- coding: utf-8 -*-
{
    'name': "Event Survey",
    'summary': """
    create survey in event
        """,
    'description': """create survey in event""",
    'author': "Bamidele Ojomo",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','event','survey'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}