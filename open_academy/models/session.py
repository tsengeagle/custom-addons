# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.session'

    name = fields.Char(required=True, size=10)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    seats = fields.Integer(string='Number of seats')

    instructor_id = fields.Many2one('res.partner', string='講師')
    course_id = fields.Many2one('open_academy.course', ondelete='cascade', string='課程', required=True)
