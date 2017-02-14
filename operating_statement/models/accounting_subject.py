# -*- coding:utf-8 -*-

from odoo import models, fields, api


class AccountingSubject(models.Model):
    _name = 'operating_statement.accounting_subject'
    # _order = 'account_id' + 'entries_id'
    name = fields.Char('會計科目名稱', size=40)
    account_id = fields.Char('會計科目代碼', size=6)
    entries_id = fields.Char('分戶代碼', size=10)
    entries_name = fields.Char('分戶名稱', size=40)
