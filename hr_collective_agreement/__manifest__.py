# -*- coding: utf-8 -*-
#   Copyright (C) 2017 EBII (http://www.saaslys.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "HR collective agreement",

    'summary': """
        HR collective agreement for OCA""",

    'description': """
        HR collective agreement for OCA
    """,

    'author': "MonsieurB Saaslys <monsieurb@saaslys.com>",
    'website': "https://www.saaslys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/collective_agreement.xml',
        'views/group_level_coef.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'test': [
    ],
    'installable': True,
}
