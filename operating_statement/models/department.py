# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'operating_statement.department'
    name = fields.Char('單位名稱', size=30)
    cost_id = fields.Char('成本中心代碼', size=6)
    account_id = fields.Char('分攤會計科目', size=6)
    account_name = fields.Char('分攤科目名稱', size=20)
    comment = fields.Text('備註', size=100)
