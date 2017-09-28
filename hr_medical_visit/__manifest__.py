# -*- coding: utf-8 -*-
#   Copyright (C) 2017 EBII (http://www.saaslys.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "HR Medical Visit",

    'summary': """
        HR Medical Visit""",

    'description': """
        HR Medical Visit
    """,

    'author': "Saaslys",
    'website': "https://www.saaslys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/hr_health_center.xml',
        'views/hr_health_center_registration.xml',
        'views/hr_medical_visit.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
