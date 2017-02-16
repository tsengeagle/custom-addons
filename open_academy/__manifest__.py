# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        練習模組""",

    'description': """
        一個模擬選課系統
    """,

    'author': "tseng",
    'website': "http://www.mytest.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/main_view.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/todo_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
