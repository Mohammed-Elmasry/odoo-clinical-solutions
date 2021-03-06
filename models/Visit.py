from odoo import models, fields, api
import datetime
import requests
import json


class Visit(models.Model):
    _name = 'visit.model'
    _description = "visits that will be related to patients in the Clinic"
    doctor = fields.Many2one('doctor.info.model', domain="[('role', '=', 'doctor')]")
    patient = fields.Many2one('odoo.clinic.patient')
    services_and_products = fields.Many2one('product.template')
    sales_price = fields.Float(related="services_and_products.list_price", string="Service Price"
                               , help="Service and Product Price Related to Doctor's Services")
    patient_name = fields.Char(related="patient.name", string="Patient Name", help="Name of Patient")
    patient_name_computed = fields.Char(string="Patient Name", compute="get_patient_name", store=True)
    visit_id = fields.Char(string="Visit ID", help="Auto Increment")
    product_name = fields.Char(related="services_and_products.name")
    product_name_computed = fields.Char(compute="get_product_and_services_name"
                                        , store=True, string="Service and Product Name",
                                        help="Product or Service  Name")
    doctor_name = fields.Char(related="doctor.name", string="Doctor Name", help="Doctor Name")
    visit_count = fields.Integer(string="Visit Count", help="To Display The Count Visits in The Clinic "
                                 , compute="count_visits")
    start_time = fields.Datetime()
    visit_type = fields.Selection([('type1', 'Medical consultation'), ('type2', 'Check Up')], string="Visit Type"
                                  , help="To Detect The Type Of Visit")
    end_time = fields.Datetime(compute='calculate_end_time')
    patient_class = fields.Selection([('class1', 'Walking Patient'), ('class2', 'Insurance Patient')]
                                     , string="Patient class", required='true', default="class1")
    name = fields.Integer(string="Set ID")
    # change the name of this field to can display it as default when create visit
    assigned_patient_location = fields.Text(string="Assigned Location")
    admission_type = fields.Char(string="Admission Type")
    preadmit_number = fields.Integer(string="Preadmit Number")
    prior_patient_location = fields.Text(string="Prior Location")
    attending_doctor = fields.Char(string="Attending doctor", help="Attending Doctor for This Visit"
                                   , compute="assign_doctor_name_to_attending_doctor", store=True)
    referring_doctor = fields.Char(string="Referring Doctor", help="Referring Doctor it is related"
                                                                   " to Doctors Out Side Our Clinic")
    hospital_service = fields.Selection([('MED', 'Medical Service'),
                                         ('SUR', 'Surgical Service'),
                                         ('URO', 'Urology Service'),
                                         ('PUL', 'Pulmonary Service'),
                                         ('CAR', 'Cardiac Service')
                                         ], string="Hospital Service")
    temporary_location = fields.Text(string="Temporary Location")
    prior_temporary_location = fields.Text(string="Previous Temporary Location")
    preadmit_test_indicator = fields.Char(string="Preadmit Test Indicator")
    re_admission_indicator = fields.Char(string="Re-Admission Indicator")
    admit_source = fields.Selection([('value', 'No suggested values defined')], string="Admit Source")
    ambulatory_status = fields.Selection([('A0', 'No functional limitations'),
                                          ('A1', 'Ambulates with assistive device'),
                                          ('A2', 'Wheelchair/stretcher bound'),
                                          ('A3', 'Comatose; non-responsive'),
                                          ('A4', 'Disoriented'),
                                          ('A5', 'Vision impaired'),
                                          ('A6', 'Hearing impaired'),
                                          ('A7', 'Speech impaired'),
                                          ('A8', 'Non-English speaking'),
                                          ('A9', 'Functional level unknown'),
                                          ('B1', 'Oxygen therapy'),
                                          ('B2', 'Special equipment (tubes, IVs, catheters)'),
                                          ('B3', 'Amputee')], string="Ambulatory Status")
    vip_indicator = fields.Char(string="VIP-Type")
    admitting_doctor = fields.Many2one('doctor.info.model', string="Admitting Doctor"
                                       , help="This field contains the admitting physician information."
                                       , domain="[('role', '=', 'doctor')]", store=True)
    patient_type = fields.Selection([('value', 'No suggested values defined')])
    visit_number = fields.Integer(string="Visit Number",
                                  help="This field contains the unique number assigned to each patient visit.")
    financial_class = fields.Selection([('value', 'No suggested values defined')], string="Financial Class"
                                       , help="    This field contains the financial class(es)"
                                              " assigned to the patient for the purpose of identifying"
                                              " sources of reimbursement")
    charge_price_indicator = fields.Selection([('value', 'No suggested values defined')], string="Charge Price Code"
                                              , help="This field contains the code used to determine which"
                                                     " price schedule is to be used for room and bed charges.")
    courtesy_code = fields.Selection([('value', 'No suggested values defined')], string="Courtesy Code")
    credit_rating = fields.Selection([('value', 'No suggested values defined')], string="Credit Rating"
                                     , help="This field contains the user-defined code to determine past"
                                            " credit experience")
    contract_code = fields.Selection([('value', 'No suggested values defined')], string="Contract Code"
                                     , help="This field identifies the type of contract entered into by "
                                            "the health care facility and the guarantorfor the purpose of "
                                            "settling outstanding account balances.")
    contract_effective_date = fields.Date(string="Contract Date", help="This field contains the date that"
                                                                       " the contract is to start or started.")
    contract_amount = fields.Integer(string="Contract Amount", help="This field contains the amount to be"
                                                                    " paid by the guarantor each period according"
                                                                    " to the contract.")
    contract_period = fields.Integer(string="Contract Period", help="This field contains the amount to"
                                                                    " be paid by the guarantor each period"
                                                                    " according to the contract.")
    interest_code = fields.Selection([('value', 'No suggested values defined')], string="Interest Amount"
                                     , help="This field indicates the amount of interest that will be charged")
    transfer_bad_debt_code = fields.Selection([('value', 'No suggested values defined')], string="Bad Debt Code"
                                              , help="This field indicates that the account was transferred"
                                                     " to bad debts and gives the reason.")
    transfer_bad_debt_date = fields.Date(string="Bad Debt Date", help="This field contains the date that "
                                                                      "the account was transferred to a bad"
                                                                      " debt status.")
    bad_debt_agency_code = fields.Integer(string="Bad Debt Agency Code")

    bad_debt_transfer_amount = fields.Integer(string="Amount of Bad Debt Transfer")
    bad_debt_recovery_amount = fields.Integer(string="Amount of Bad Debt Recovery")
    delete_account_indicator = fields.Selection([('value', 'No suggested values defined')],
                                                string="Delete Account Indicator"
                                                , help="This field indicates that the account was deleted from "
                                                       "the file")
    delete_account_indicator_reasons = fields.Text(string="Reasons Of Delete Account"
                                                   , help="gives the reason for delete the account ")
    delete_account_date = fields.Date(string="Delete Account Date")
    discharge_disposition = fields.Selection([('value', 'No suggested values defined')], string="Discharge Disposition")
    discharged_location = fields.Text(string="Discharged Location"
                                      , help="This field indicates the health care "
                                             "facility to which the patient was discharged and the date.")
    diet_type = fields.Selection([('value', 'No suggested values defined')])
    servicing_facility = fields.Selection([('value', 'No suggested values defined')], string="Servicing Facility")
    account_status = fields.Selection([('value', 'No suggested values defined')], string="Account Status")
    pending_location = fields.Text(string="Pending Location")
    admit_date = fields.Datetime(string="Admit Date/Time")
    discharge_date = fields.Datetime(string="Discharge Date/Time")
    current_patient_balance = fields.Integer(string="Current Balance", compute='calculate_current_patient_balance'
                                             , help="it is the visit balance Computed Field"
                                                    "To Display Difference between Payment and "
                                                    "total Charges")
    total_charges = fields.Integer(string="Total Visit Charges", compute="get_current_charges"
                                   , help="This field contains the total visit charges.")
    total_adjustments = fields.Integer(string="Total Adjustments", help="This field contains the total adjustments "
                                                                        "for visit.", compute="get_total_adjustments")
    total_payments = fields.Integer(string="Total Payment", help="This field contains the total payments for visit.")
    alternate_visit_id = fields.Selection([('BCV', 'Bank Card Validation Number'),
                                           ('NPI', 'Check digit algorithm in the US National Provider Identifier'),
                                           ('ISO', 'ISO 7064: 1983'),
                                           ('M10', 'Mod 10 algorithm'),
                                           ('M11', 'Mod 11 algorithm'),
                                           ('ACSN', 'Accession ID'),
                                           ('AM', 'American Express'),
                                           ('AMA', 'American Medical Association Number'),
                                           ('AN', 'Account number'),
                                           ('ANON', 'Anonymous identifier'),
                                           ('ANC', 'Account number Creditor'),
                                           ('AND', 'Account number debitor'),
                                           ('ANT', 'Temporary Account Number'),
                                           ('APRN', 'Advanced Practice Registered Nurse number'),
                                           ('ASID', 'Ancestor Specimen ID'),
                                           ], string="Alternate Visit ID")
    visit_indicator = fields.Selection([('A', 'Account level (default)'),
                                        ('V', 'Visit level')], string="Visit Indicator", default='A')
    service_episode_description = fields.Text(string="Service Description")
    service_episode_identifier = fields.Integer(string="Service Identifier")
    count = fields.Integer(help="Count use for computed field visit count")
    patient = fields.Many2one('odoo.clinic.patient')
    visit_status = fields.Selection([('Draft', 'Draft'), ('Comfirmed', 'Comfirmed'), ('Inplace', 'Inplace'),
                                     ('Inprogress', 'Inprogress'), ('Done', 'Done'), ('Canceled', 'Canceled')]
                                    , default='Draft')
    sheet = fields.One2many('odoo.clinic.medical', 'visit')

    @api.model
    def create(self, vals):

        vals['visit_id'] = self.env['ir.sequence'].next_by_code('clinic.visit')
        vals['name'] = self.env['ir.sequence'].next_by_code('set_id')
        res = super(Visit, self).create(vals)
        return res

    @api.depends('start_time')
    def calculate_end_time(self):

        for visit in self.filtered('start_time'):
            delta = datetime.timedelta(minutes=30)
            visit.end_time = visit.start_time + delta

    # Computed method to get the current charges of this visit
    @api.depends('sales_price')
    def get_current_charges(self):

        for visit in self.filtered('sales_price'):
            visit.total_charges = visit.sales_price

    # Computed method to Calculate the current patient balance from remove total charges and total adjustments
    # from total payments
    @api.depends('total_charges', 'total_payments')
    def calculate_current_patient_balance(self):

        for visit in self.filtered('total_charges'):
            visit.current_patient_balance = visit.total_payments - visit.total_charges - visit.total_adjustments

    @api.depends('doctor')
    def assign_doctor_name_to_attending_doctor(self):

        for visit in self.filtered('doctor'):
            visit.attending_doctor = visit.doctor_name

    @api.depends('patient_name')
    def get_patient_name(self):

        for visit in self.filtered('patient_name'):
            visit.patient_name_computed = visit.patient_name

    @api.depends('total_charges')
    def get_total_adjustments(self):

        for visit in self.filtered('total_charges'):
            visit.total_adjustments = visit.total_charges * (-0.1)

    @api.depends('product_name')
    def get_product_and_services_name(self):

        for visit in self.filtered('product_name'):
            visit.product_name_computed = visit.product_name

    def count_visits(self):

        for visit in self:
            visits = self.env['visit.model'].search(args=[])
            count = len(visits)
            visit.count = count
            visit.visit_count = visit.count

    @api.onchange('visit_status')
    def on_change_state(self):
        print (self.visit_status)
        if self.visit_status=="Comfirmed":
            try:
                url = 'https://fcm.googleapis.com/fcm/send'
                payload = {
                  "notification": {
                   "title": "Hello "+self.patient.name,
                   "body": "welcome to our clinic your visit is confirmed in " +str(self.start_time)
                  },
                  "to" : "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
                }
                headers = {'content-type': 'application/json','Authorization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}


                r = requests.post(url, data=json.dumps(payload), headers=headers)
                print(r.json)
            except:
                pass
        if self.visit_status=="Done":
            try:
                url = 'https://fcm.googleapis.com/fcm/send'
                payload = {
                  "notification": {
                   "title": "Hello "+self.patient.name,
                   "body": "Thank you for attend in time and now you can see all details about visit "
                  },
                  "to" : "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
                }
                headers = {'content-type': 'application/json','Aut'
                                                              'horization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}


                r = requests.post(url, data=json.dumps(payload), headers=headers)
                print(r.json)
            except:
                pass

        if self.visit_status == "Inplace":
            medical=self.env['odoo.clinic.medical'].search(args=[('visit', '=',self.name)])
            if not medical.exists() :
                medical=self.env['odoo.clinic.medical'].create({"visit":self.name})
                print (medical.visit_status)
                print("kk",self.name)

    @api.multi
    def cancel_visit(self):
        # visit=self.env['visit.model'].write({"visit_status": "Canceled"})
        # self.visit_status="Canceled"
        for rec in self:
            rec.write({'visit_status': 'Canceled'})
        try:
            url = 'https://fcm.googleapis.com/fcm/send'
            payload = {
                "notification": {
                    "title": "Hello " + self.patient.name,
                    "body": "We are very sorry this visit is canceled "
                },
                "to": "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
            }
            headers = {'content-type': 'application/json', 'Aut'
                                                           'horization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print(r.json)
        except:
            pass
    @api.multi
    def button_done(self):
       for rec in self:
           rec.write({'visit_status': 'Done'})

       try:
            url = 'https://fcm.googleapis.com/fcm/send'
            payload = {
                "notification": {
                    "title": "Hello " + self.patient.name,
                    "body": "Thank you for attend in time and now you can see all details about visit "
                },
                "to": "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
            }
            headers = {'content-type': 'application/json', 'Aut'
                                                           'horization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print(r.json)
       except:
            pass

    @api.multi
    def button_cancel(self):
        for rec in self:
            rec.write({'visit_status': 'Canceled'})
        try:
            url = 'https://fcm.googleapis.com/fcm/send'
            payload = {
                "notification": {
                    "title": "Hello " + self.patient.name,
                    "body": "We are very sorry this visit is canceled "
                },
                "to": "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
            }
            headers = {'content-type': 'application/json', 'Aut'
                                                           'horization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print(r.json)
        except:
            pass
    @api.multi
    def button_reset(self):
           for rec in self:
               rec.write({'visit_status': 'Draft'})
    @api.multi
    def button_confirmed(self):
        for rec in self:
                rec.write({'visit_status': 'Comfirmed'})
        # firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
        # result = firebase.get('/user001', {'body': "welcome to our clinic your visit is confirmed in " ,
        #                                    'title': "Hello " ,})
        # print (result)

        try:
            url = 'https://fcm.googleapis.com/fcm/send'
            payload = {
                "notification": {
                    "title": "Hello " + self.patient.name +str(datetime.datetime.now()),
                     "body": "welcome to our clinic your visit is confirmed in " + str(self.start_time),
                    "date":str(datetime.datetime.now())
                },
                "to": "evdWKI15D-0:APA91bEL-aQglC_TLmmuW-f5DZwx-Kvc_vNVPCdYtRYxiegGi-y6DovlzMkd-gsf_3hmpQ_U34aWbMmoIfHFOFz4pPTLVYUiVGYmEVSUDkJRo1BlTxsr0AGPIEijFFp0IjWEZfKf1EQn"
            }
            headers = {'content-type': 'application/json',
                       'Authorization': 'key=AAAAhnraShA:APA91bFZvJR5Y1KlMPSyORRdAuLaWD4zQ61jzwt_AjXFqPYbROO23e1gmbrUysHNURvpGFP7EPFUIMl_SUwCvBWSFtympRs6uFy1W_yE40ivfr9YP_I1SfJQVqXtdzQkPNd-ByA5aBjU'}

            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print(r.json)
        except:
            pass


    @api.multi
    def button_inplace(self):
        for rec in self:
            rec.write({'visit_status': 'Inplace'})
        medical=self.env['odoo.clinic.medical'].create({"visit":self.id,"patient":self.patient.id})
        print("kk",self.name)

    @api.multi
    def button_inprogress(self):
           for rec in self:
               rec.write({'visit_status': 'Inprogress'})
