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
                 "gender": records[i]["gender"], "title": records[i]["job_title"], "rank": records[i]["certificate"],"rate":3})
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

        params = http.request.httprequest.data
        print(params)
        params = json.loads(params)
        time_slot = datetime.datetime.strptime((params["doc_date"] + " " + params["doc_time"]), "%m/%d/%Y %I:%M %p")
        CONST_EG_TIME_REMOVAL = datetime.timedelta(minutes = 120)
        start_time = time_slot - CONST_EG_TIME_REMOVAL
        end_time = time_slot + datetime.timedelta(minutes=30) - CONST_EG_TIME_REMOVAL

        http.request.env['visit.model'].sudo().create({
             'doctor': params["doc_id"],
             "start_time": start_time,
             'patient_class': 'OBGYN',
             "end_time": end_time,
             "patient":params["pat_id"],
             "visit_status":"Draft"
             })
        # new_record.sudo().write()
        return json.dumps("visit scheduled successfully")



    @http.route('/clinical_management_system/get_empty_slots/', auth="none", type="http", methods=['get'], cors="*")
    def get_empty_time_slots(self):
        """
        :return: a list of available time slots
        """
        doctors = http.request.env["doctor.info.model"].sudo().search([('role','=','doctor')])
        week = get_current_week_days()
        result = []
        names = []
        appointments = []
        potential_session_times = []
        for day in week:
            potential_session_times.extend(get_dates(day))

        for day in week:
            for doctor in doctors:
                for session in potential_session_times:
                    if is_free(doctor, session) and session.date() == day:
                        appointments.append(session.strftime("%I:%M %p"))
                names.append({"id": doctor.id,"name": doctor.name, "appointments": appointments})
                appointments = []
            result.append({"date": day.strftime("%m/%d/%Y"), "doctors" : names})
            names = []

        print(result)
        return json.dumps(result)

    @http.route('/clinical_management_system/get_visits', auth="none", type="http", methods=["get"], cors="*")
    def get_visits(self):
        # {'doc_name': 'Mohamed', 'doc_id': `'1', 'doc_date': '10/6/2019', 'doc_time': '8-2', 'pat_id': 0}
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


def get_dates(date):
    """
    :return: a list of the available time slots for the upcoming week
    """
    session_times = ['10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '12:30 PM', '01:00 PM', '01:30 PM', '02:00 PM']
    empty_time_slots = []

    #concat the slots to given date
    for slot in session_times:
        empty_time_slots.append(datetime.datetime.strptime(date.strftime("%m/%d/%Y") + " " + slot, "%m/%d/%Y %I:%M %p"))

    return empty_time_slots


def get_current_week_days():
    """
    :return: a list of 5 datetime objects representing days of the current week (starting today)
    """
    dates = []
    day = datetime.timedelta(days=1)
    today = datetime.datetime.today()
    if today.strftime("%a") not in ("Fri", "Sat"):
        dates.append(today.date())  # first day of week
    # loop to calculate a whole week from today
    next_day = today
    for i in range(5):
        next_day = next_day + day
        if next_day.strftime("%a") not in ("Sat", "Fri"):
            dates.append(next_day.date())
    return dates



def is_free(doctor, time):
    """
    :param doctor: given doctor object
    :param time: given datetime object
    :return: boolean denoting whether given doctor is available at the given time
    """
    visits = http.request.env['visit.model'].sudo().search([('doctor','=',doctor.id)])
    #get time stamps for each visit
    stamps = []
    for visit in visits:
        stamps.append(visit.start_time + datetime.timedelta(minutes=120))
    return time not in stamps
