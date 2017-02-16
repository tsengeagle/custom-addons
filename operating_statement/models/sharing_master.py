# -*- coding:utf-8 -*-

from odoo import models, fields, api


class SharingMaster(models.Model):
    _name = 'operating_statement.sharing_master'

    department_id = fields.Many2one('operating_statement.department', ondelete='set null', string='成本中心')
    accounting_id = fields.Many2one('operating_statement.accounting_subject', ondelete='set null', string='分攤會計科目')
    sharing_method = fields.Char(string='分攤方法', size=20)
    sequence = fields.Integer(string='順序', default=0, required=True)
    is_disable = fields.Boolean(string='停用?', default=False)
