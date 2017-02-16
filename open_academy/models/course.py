# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    name = fields.Char(string='課程名稱', size=10, required=True)
    description = fields.Text(string='描述', size=100)
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='負責人', index=True)
