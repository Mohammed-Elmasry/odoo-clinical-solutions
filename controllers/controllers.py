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

    @http.route('/clinical_management_system/doctor', type="http", auth="none", methods=['get'])
    def get_doctor(self, doctor_id):
        record = http.request.env['doctor.info.model'].sudo().browse(int(doctor_id))
        return (record.gender)

    @http.route('/clinical_management_system/doctor/<model("doctor.info.model"):doctor>/', type="http", auth="none")
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
        print("dsfs",kw)
        return json.dumps("shokran")


    @http.route('/clinical_management_system/patient', type="http", auth="none", methods=['get'], cors="*")
    def get_patient(self, patient_id):
        record = http.request.env['odoo.clinic.patient'].sudo().browse(int(patient_id))
        patient={}
        data = []
        print(record.visit[1].doctor.name)
        data.append({"id":record.id})
        #
        for t in range(len(record.visit)):
            print(record.visit[t].visit_number)
            data.append({
                        "visit_start_time "+str(t) :str(record.visit[t].start_time),
                         "visit_id "+str(t) :record.visit[t].visit_number,
                         "visit_DOCTOR "+str(t) :record.visit[t].doctor.name})
        return json.dumps(data)



    @http.route('/clinical_management_system/patient/<model("odoo.clinic.patient"):patient>/', type="http",
                auth="none", cors="*")
    def get_patient_data(self, patient):
        return self.get_patient(patient.id)

    @http.route('/clinical_management_system/patients/', type="http", auth="public", methods=['get'])
    def get_patients(self):

        records = http.request.env["odoo.clinic.patient"].sudo().search([])
        result = []
        patients = []
        for i in range(len(records)):
            for attr in ["name", "phone"]:
                patients.append(
                    {"patient %s " % str(attr): records[i][attr]})  # , {"doctor gender": records[i].gender},
                # {"doctor license": records[i].license_id})
        result.append(patients)
        print(patients)

        return json.dumps(patients)



    @http.route('/clinical_management_system/medical/patient', type="http", auth="none", methods=['get'], cors="*")
    def get_medical(self, patient_id):
        record = http.request.env['odoo.clinic.patient'].sudo().browse(int(patient_id))
        medical = []
        for t in range(len(record.medical)):
            print(record.medical[t].dm)
            medical.append({"history "+str(t) :record.medical[t].obstetric_gynecological_history,
                            "dm "+str(t) :record.medical[t].dm,
                            "htn "+str(t) :record.medical[t].htn,
                            "cardiac "+str(t) :record.medical[t].cardiac,
                            "heptic " + str(t): record.medical[t].heptic,
                            "renal " + str(t): record.medical[t].renal,
                            "others " + str(t): record.medical[t].others,
                            "surgical_history " + str(t): record.medical[t].surgical_history,
                            "bp " + str(t): record.medical[t].bp,
                            "rr " + str(t): record.medical[t].rr,
                            "hr " + str(t): record.medical[t].hr,
                            "temp " + str(t): record.medical[t].temp,
                            "fhc " + str(t): record.medical[t].fhc,
                            "weight " + str(t): record.medical[t].weight,
                            "examination " + str(t): record.medical[t].examination,
                            "drug_allergy " + str(t): record.medical[t].drug_allergy,
                            })
        return json.dumps(medical)



    @http.route('/clinical_management_system/medical/patient/<model("odoo.clinic.patient"):patient>/', type="http",
                auth="none" , cors="*"  )
    def get_patient_medical(self, patient):
        return self.get_patient(patient.id)

    @http.route('/clinical_management_system/patient/new/', type="http", auth="none", methods=['POST'], cors="*",
                csrf=False)
    def create_patient(self, **params):
        ee = json.loads(http.request.httprequest.data)
        print (ee["name"])
        print(json.loads(http.request.httprequest.data))
        #
        record = http.request.env['odoo.clinic.patient'].sudo().create(
            {"name": ee["name"], "email": ee["email"], "phone": ee["phone"]
                , "city": ee["city"], "date": ee["date"]
                , "gender": ee["gender"], "token": ee["token"]})
        return json.dumps(record.id)
        # return json.dumps(record.id)


