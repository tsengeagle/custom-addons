# -*- coding: utf-8 -*-
from odoo import http

# class DeptReport(http.Controller):
#     @http.route('/dept_report/dept_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dept_report/dept_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dept_report.listing', {
#             'root': '/dept_report/dept_report',
#             'objects': http.request.env['dept_report.dept_report'].search([]),
#         })

#     @http.route('/dept_report/dept_report/objects/<model("dept_report.dept_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dept_report.object', {
#             'object': obj
#         })