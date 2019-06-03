# -*- coding: utf-8 -*-
from odoo import http
import json
class ClinicalManagementSystem(http.Controller):
    @http.route('/clinical_management_system/clinical_management_system/', auth='public')
    def index(self, **kw):
        request = http.request
        vals = kw.keys()
        # print("Your values are: ",vals)
        # print("Your Email is: ", kw["Email"])
        # for i in http.request.env["product.template"]:
        #     print(i)


        return json.dumps({'id': 'yy'})
    #
    #
    @http.route('/home', auth='public')
    def homer(self, **kw):
        return "hhhhhhhhhh "
    # @http.route('/list', auth='public')
    # def list(self, **kw):
    #     return http.request.render('clinical_management_system.listing', {
    #         'root': '/odoo-clinical-solutions',
    #         'objects': http.request.env['odoo.clinic.patient'].search([]),
    #     })

    # @http.route('/product/<field>/<value>', type='http', auth="public", website=True)
    # def get_product_by_name(self, field, value, **kw):
    #     assert field in ('name', 'weight')
    #     prod = http.request.env["odoo.clinic.patient"].search([(field, 'ilike', value)])
    #     if prod:
    #         return json.dumps(prod.read(['name','weight']))
    #     else:
    #         return "Product not found"
    #
    # @http.route('/clinical_management_system/clinical_management_system/objects/<model("clinical_management_system.clinical_management_system"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('clinical_management_system.object', {
    #         'object': obj
    #     })
# #
# class Example(http.Controller):
#     @http.route('/example', type='http', auth='public', website=True)
#     def render_example_page(self):
#         return http.request.render('create_webpage_demo.example_page', {})

   # @http.route('/clinical_management_system/clinical_management_system/doctors/', auth='user')
   #  def get_doctors(self, **kw):
   #
   #      return http.request.render('clinical_management_system.listing' ,{
   #          'root': '/clinical_management_system/clinical_management_system',
   #          'objects': http.request.env['doctor.info.model'].search([])
   #      })



# class ClinicalManagementSystem(http.Controller):
#     @http.route('/clinical_management_system/clinical_management_system/', auth='public')
#     def index(self, **kw):
#         request = http.request
#         vals = kw.keys()
#         # print("Your values are: ",vals)
#         # print("Your Email is: ", kw["Email"])
#         # for i in http.request.env["product.template"]:
#         #     print(i)
#         return json.dumps({'id': 'yy'})
#
#     @http.route('/clinical_management_system/clinical_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-clinical-solutions.listing', {
#             'root': '/clinical_management_system/clinical_management_system',
#             'objects': http.request.env['res.partner'].search([]),
#         })
#
#     @http.route(
#         '/clinical_management_system/clinical_management_system/objects/<model("clinical_management_system.clinical_management_system"):obj>/',
#         auth='public')
#     def object(self, obj, **kw):  ##this is a particular object
#         return http.request.render('clinical_management_system.object', {
#             'object': obj
#         })
#
#     @http.route('/clinical_management_system/clinical_management_system/doctors/', auth='public')
#     def get_doctors(self, **kw):
#         return http.request.render('clinical_management_system.listing', {
#             'root': '/clinical_management_system/clinical_management_system',
#             'objects': http.request.env['doctor.info.model'].sudo().search([])
#         })

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

    @http.route('/clinical_management_system/doctor', type="http", auth="none", methods=['get'])
    def get_doctor(self, doctor_id):
        record = http.request.env['doctor.info.model'].sudo().browse(int(doctor_id))
        print(record)
        data=[record.name,record.license_id]
        return json.dumps(data)

    @http.route('/clinical_management_system/doctor/<model("doctor.info.model"):doctor>/', type="http", auth="none")
    def get_doctor_path(self, doctor):
        return self.get_doctor(doctor.id)
    #
    # @http.route('/clinical_management_system/doctors/', type="http", auth="public", methods=['get'])
    # def get_doctors(self):
    #     """
    #         @
    #     :return: returns all employees that have the role of 'doctor'
    #     """
    #     records = http.request.env["doctor.info.model"].sudo().search(args=[('role', '=', 'doctor')])
    #     result = []
    #     doctors = []
    #     for i in range(len(records)):
    #         for attr in ["name", "license_id", "gender"]:
    #             doctors.append({"doctor %s " % attr: records[i][attr]})  # , {"doctor gender": records[i].gender},
    #             # {"doctor license": records[i].license_id})
    #     result.append(doctors)
    #     print(doctors)
    #     return json.dumps(doctors)
    @http.route('/clinical_management_system/doctors/', type="http", auth="public", methods=['get'], cors="*")
    def get_doctors(self):
        """
        :return: returns all employees that have the role of 'doctor'
        """
        records = http.request.env["doctor.info.model"].sudo().search(args=[('role', '=', 'doctor')])
        doctor = {}
        result = []
        for i in range(len(records)):
            result.append(
                {"id": records[i]["id"], "name": records[i]["name"], "license number": records[i]["license_id"],
                 "gender": records[i]["gender"], "title": records[i]["job_title"],
                 "rank": records[i]["certificate"]})

        return json.dumps(result)

    @http.route('/clinical_management_system/officers/', type="http", auth="public", methods=['get'])
    def get_officers(self):
        """
        :return: returns all employees of the role 'officer'
        """
        records = http.request.env["doctor.info.model"].sudo().search(args=[('role', '=', 'officer')])
        result = []
        officers = []
        for i in range(len(records)):
            for attr in ["name", "license_id", "gender"]:
                officers.append(
                    {"officer %s " % str(attr): records[i][attr]})  # , {"doctor gender": records[i].gender},
                # {"doctor license": records[i].license_id})
        result.append(officers)
        print(officers)


        return json.dumps(officers)










    @http.route('/clinical_management_system/patient', type="http", auth="none", methods=['get'])
    def get_patient(self, patient_id):
        record = http.request.env['odoo.clinic.patient'].sudo().browse(int(patient_id))
        data=[]
        # , record.visit.start_datetime
        data = [record.name,record.weight]
        # d={"patient name" :record.name}

        return json.dumps(data)

        # return json.dumps(data)
        # return {'name':record.name}

    @http.route('/clinical_management_system/patient/<model("odoo.clinic.patient"):patient>/', type="http", auth="none")
    def get_patient_data(self, patient):
        return self.get_patient(patient.id)

    @http.route('/clinical_management_system/patients/', type="http", auth="public", methods=['get'])
    def get_patients(self):

        records = http.request.env["odoo.clinic.patient"].sudo().search([])
        result = []
        patients = []
        for i in range(len(records)):
            for attr in ["name", "phone"]:
                patients.append({"patient %s " % str(attr): records[i][attr]})  # , {"doctor gender": records[i].gender},
                # {"doctor license": records[i].license_id})
        result.append(patients)
        print(patients)
        return json.dumps(patients)
