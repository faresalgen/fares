# -*- coding: utf-8 -*-
{
    'name': 'Mange Hospital',
    'version': '15.0.0.0.1',
    'summary': 'Mange Hospital',
    'description': """Mange Hospital""",
    'category': 'Tutorials',
    'author': 'Odoo Fares',
    'maintainer': 'Odoo Fares',
    'license': 'AGPL-3',
    'depends': [
                 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
   
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
