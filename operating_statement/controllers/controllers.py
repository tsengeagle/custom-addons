# -*- coding: utf-8 -*-
from odoo import http

# class OperatingStatement(http.Controller):
#     @http.route('/operating_statement/operating_statement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/operating_statement/operating_statement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('operating_statement.listing', {
#             'root': '/operating_statement/operating_statement',
#             'objects': http.request.env['operating_statement.operating_statement'].search([]),
#         })

#     @http.route('/operating_statement/operating_statement/objects/<model("operating_statement.operating_statement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('operating_statement.object', {
#             'object': obj
#         })