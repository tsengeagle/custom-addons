# -*- coding: utf-8 -*-
from odoo import http

# class SectionStatment(http.Controller):
#     @http.route('/section_statment/section_statment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/section_statment/section_statment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('section_statment.listing', {
#             'root': '/section_statment/section_statment',
#             'objects': http.request.env['section_statment.section_statment'].search([]),
#         })

#     @http.route('/section_statment/section_statment/objects/<model("section_statment.section_statment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('section_statment.object', {
#             'object': obj
#         })