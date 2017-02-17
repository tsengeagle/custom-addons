# -*- coding: utf-8 -*-
{
    'name': "Operating Statement",

    'summary': """
        科經營報表系統
        """,

    'description': """
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
        'views/operating_statement_view.xml',
        'views/department_view.xml',
        'views/accounting_subject_view.xml',
        'views/sharing_master_view.xml',
        'views/report_interval_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
