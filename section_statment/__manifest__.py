# -*- coding: utf-8 -*-
{
    'name': "SectionStatment",

    'summary': """
        科經營報表系統
        """,

    'description': """
        透過預設分攤原則，計算各單位損益
    """,

    'author': "tsengeagle",
    'website': "http://www.tzuchi.com.tw",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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