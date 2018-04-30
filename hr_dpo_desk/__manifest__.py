# -*- coding: utf-8 -*-
{
    'name': "Data Protector Officer",

    'summary': """
        Framework desktop for DPO usage""",

    'description': """
        DPO View for RGPD 2018""",


    'author': "EBII",
    'website': "https://www.saaslys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
         'views/views.xml',
         'security/hr_dpo_security.xml',
         'security/ir.model.access.csv',
         'data/data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'test': [
    ],
    'installable': True,
}




