# -*- encoding: UTF-8 -*-

{
    'name': 'Event Registration Form',
    'version': '10.1.0',
    'author': 'Laxicon Solution',
    'sequence': 10,
    'category': 'event',
    'website': "www.laxicon.in",
    'license': 'LGPL-3',
    'support': 'info@laxicon.com',
    'description': """Create new attendee’s data by adding more fields.
    """,
    'depends': ['event', 'hr_attendance', 'website', 'website_event', 'event_sale'],
    'data': [
        'views/website_reg_qty.xml',
        'views/event_att_form.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
