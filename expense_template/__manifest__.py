# -*- coding: utf-8 -*-
{
    'name': "expense_template",

    'summary': """
        
        """,

    'description': """
        
    """,

    'author': "Hashmicro / PYVTech - Yajushi",
    'website': "http://www.hashmicro.com",

    'category': 'Event',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['event','hr_expense'],

    # always loaded
    'data': [
        'views/expense_template_view.xml',
    ],
}
