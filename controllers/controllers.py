# -*- coding: utf-8 -*-
from odoo import http, fields
import json, datetime

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

    @http.route('/clinical_management_system/doctor/<model("doctor.info.model"):doctor>/', type="http", auth="none",
                cors="*")
    def get_doctor_path(self, doctor):
        return self.get_doctor(doctor.id)

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
                 "gender": records[i]["gender"], "title": records[i]["job_title"], "rank": records[i]["certificate"]})
        return json.dumps(result)

    @http.route('/clinical_management_system/officers/', type="http", auth="public", methods=['get'], cors="*")
    def get_officers(self):
        """
        :param: this function takes nothing
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

    @http.route('/clinical_management_system/schedule_visit/', type="http", auth="none", methods=['post'], cors="*",
                csrf=False)
    def schedule_visit(self, **kw):

        # {'doc_name': 'Mohamed', 'doc_id': '1', 'doc_date': '10/6/2019', 'doc_time': '8-2', 'pat_id': 0}
        time_slots = ['10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '12:30 PM', '01:00 PM', '01:30 PM',
                      '02:00 PM']
        params = http.request.httprequest.data
        print(params)
        params = json.loads(params)
        time_slot = datetime.datetime.strptime((params["doc_date"] + " " + params["doc_time"]), "%m/%d/%Y %I:%M %p")
        CONST_EG_TIME_ADDITION = datetime.timedelta(minutes=30)
        end_time = time_slot + CONST_EG_TIME_ADDITION

        http.request.env['visit.model'].sudo().create({
             'doctor_id': params["doc_id"],
             'attending_doctor': params["doc_id"],
             "start_time": time_slot,
             'patient_class': 'OBGYN',
             "end_time": end_time,
             "patient":params["pat_id"],
             })
        # new_record.sudo().write()
        return json.dumps("visit scheduled successfully")

    @http.route('/clinical_management_system/get_empty_slots/', auth="none", type="http", methods=['get'], cors="*")
    def get_empty_time_slots(self):
        dates = []
        day = datetime.timedelta(days=1)
        today = datetime.datetime.today()
        dates.append(today) # first day of week
        #loop to calculate a whole week from today
        next_day = today
        for i in range(6):
            next_day = next_day + day
            if next_day.strftime("%a") not in("Sat", "Fri"):
                dates.append(next_day)
        return json.dumps("a7san naaaas")

    @http.route('/clinical_management_system/get_visits', auth="none", type="http", methods=["get"], cors="*")
    def get_visits(self):
        # {'doc_name': 'Mohamed', 'doc_id': '1', 'doc_date': '10/6/2019', 'doc_time': '8-2', 'pat_id': 0}
        visits = http.request.env["visit.model"].sudo().search([])
        for visit in visits:
            print(type(visit["start_time"]))
            CONST_EG_TIME_ADDITION = datetime.timedelta(hours=2)
            time = visit["start_time"] + CONST_EG_TIME_ADDITION
            print(visit["start_time"])
            print(time)
            twelve_hour_format = datetime.datetime.strftime(time, "%I:%M %p")
            visit_date = datetime.datetime.strftime(time, "%m/%d/%Y")
            print(twelve_hour_format)
            print(visit_date)

        # time = visits[0]["start_time"]
        # time_slots = []
        # for visit in visits:
        #     doctor = visit["attending_doctor"]
        #     fields.Datetime.from_string(visit)
        #     my_time = datetime.datetime.strftime(visits[i]["start_time"], "%m/%j/%Y %I:%M")
        #     my_date = datetime.datetime.strptime(my_time, "%m/%j/%Y %I:%M").date()
        #     my_time = datetime.datetime.strptime(my_time, "%m/%j/%Y %I:%M").time()
        #     print(type(my_time))
        #     time_slots.append([my_time.strftime("%I:%M %p"), my_date.strftime("%m/%d/%Y"),my_time.strftime("%p"), doctor.name])
        return json.dumps("wallahy gada3")
