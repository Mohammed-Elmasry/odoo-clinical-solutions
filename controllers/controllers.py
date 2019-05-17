# -*- coding: utf-8 -*-
from odoo import http

# class ClinicalManagementSystem(http.Controller):
#     @http.route('/clinical_management_system/clinical_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinical_management_system/clinical_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinical_management_system.listing', {
#             'root': '/clinical_management_system/clinical_management_system',
#             'objects': http.request.env['clinical_management_system.clinical_management_system'].search([]),
#         })

#     @http.route('/clinical_management_system/clinical_management_system/objects/<model("clinical_management_system.clinical_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinical_management_system.object', {
#             'object': obj
#         })