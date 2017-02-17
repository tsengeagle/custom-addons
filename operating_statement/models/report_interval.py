# -*- coding:utf-8 -*-

from odoo import models, fields, api


class ReportInterval(models.Model):
    _name = 'operating_statement.report_interval'

    name = fields.Char(string='報表年月', size=50)
    start_date = fields.Date(string='起始日期')
