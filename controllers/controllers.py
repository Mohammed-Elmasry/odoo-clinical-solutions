# -*- coding: utf-8 -*-
from odoo import http
import  json

class ClinicalManagementSystem(http.Controller):
    @http.route('/clinical_management_system/clinical_management_system/', auth='public')
    def index(self, **kw):
        request = http.request
        vals = kw.keys()
        # print("Your values are: ",vals)
        # print("Your Email is: ", kw["Email"])
        # for i in http.request.env["product.template"]:
        #     print(i)
        return  json.dumps({'id': 'yy'})

    @http.route('/clinical_management_system/clinical_management_system/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('clinical_management_system.listing', {
            'root': '/clinical_management_system/clinical_management_system',
            'objects': http.request.env['res.partner'].search([]),
        })

    @http.route('/clinical_management_system/clinical_management_system/objects/<model("clinical_management_system.clinical_management_system"):obj>/', auth='user')
    def object(self, obj, **kw): ##this is a particular object
        return http.request.render('clinical_management_system.object', {
            'object': obj
        })

    @http.route('/clinical_management_system/clinical_management_system/doctors/', auth='user')
    def get_doctors(self, **kw):
        return http.request.render('clinical_management_system.listing' ,{
            'root': '/clinical_management_system/doctor.info.model',
            'objects': http.request.env['doctor.info.model'].search([])
        })


    # @http.route('')