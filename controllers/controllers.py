# -*- coding: utf-8 -*-
from odoo import http
import json
from ast import literal_eval
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

    # @http.route('/clinical_management_system/clinical_management_system/objects/<model("doctor.info.model"):obj>/', auth='user')
    # def object(self, obj, **kw): ##this is a particular object
    #     return http.request.render('clinical_management_system.object', {
    #         'object': obj
    #     })

    @http.route('/clinical_management_system/doctor', type="http", auth="none", methods=['get'], cors="*")
    def get_doctor(self, doctor_id):
        record = http.request.env['doctor.info.model'].sudo().browse(int(doctor_id))
        return (record.gender)

    @http.route('/clinical_management_system/doctor/<model("doctor.info.model"):doctor>/', type="http", auth="none", cors="*")
    def get_doctor_path(self, doctor):
        return self.get_doctor(doctor.id)

    @http.route('/clinical_management_system/doctors/', type="http", auth="public", methods=['get'], cors="*")
    def get_doctors(self):
        """

        :return: returns all employees that have the role of 'doctor'
        """
        records = http.request.env["doctor.info.model"].sudo().search(args=[('role','=','doctor')])
        doctor = {}
        result = []
        for i in range(len(records)):
            result.append({"id":records[i]["id"], "name":records[i]["name"], "license number": records[i]["license_id"],
                               "gender": records[i]["gender"], "title":records[i]["job_title"], "rank":records[i]["certificate"]})
        return json.dumps(result)



    @http.route('/clinical_management_system/officers/', type="http", auth="public", methods=['get'], cors="*")
    def get_officers(self):
        """
        :param: this function takes nothing
        :return: returns all employees of the role 'officer'
        """
        records = http.request.env["doctor.info.model"].sudo().search(args=[('role','=','officer')])
        result = []
        officers = []
        for i in range(len(records)):
            for attr in ["name","license_id","gender"]:
                officers.append({"officer %s " % str(attr): records[i][attr]}) #, {"doctor gender": records[i].gender},
                           # {"doctor license": records[i].license_id})
        result.append(officers)
        print(officers)
        return json.dumps(officers)


    @http.route('/clinical_management_system/schedule_visit/', type="http", auth="none", methods=['post'], cors="*", csrf=False)
    def schedule_visit(self, **kw):
        params = http.request.params
        # print(params)
        print(params)
        return json.dumps("enahrada agazaaaaa!!")

    @http.route('/clinical_management_system/get_empty_slots/', auth="none", type="http", methods=['get'], cors="*")
    def get_empty_time_slots(self):
        print("empty slots")
        return json.dumps("empty slots")

    @http.route('/clinical_management_system/get_visits', auth="none", type="http", methods=["get"], cors="*")
    def get_visits(self):
        visits = http.request.env["visit.model"].sudo().search([])
        for i in range(len(visits)):
            print(visits[i]["patient_class"])
        # return json.dumps(visits)