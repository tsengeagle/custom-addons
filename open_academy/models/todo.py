# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Todo(models.Model):
    _name = 'open_academy.todo'

    name = fields.Char('Todo', size=20, required=True)
    description = fields.Text('description', size=100)
    is_done = fields.Boolean('Done?', default=False)
    is_active = fields.Boolean('Active?', default=True)

    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
