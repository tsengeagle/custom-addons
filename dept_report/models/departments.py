# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'dept_report.department'

    name = fields.Char(size=20)
    costNo = fields.Char(string="Cost id")
    comment = fields.Text()
