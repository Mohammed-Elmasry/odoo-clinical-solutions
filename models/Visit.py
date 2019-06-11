from odoo import models, fields, api


class Visit(models.Model):
    _name = 'visit.model'
    # _rec_name = 'set_id'

    doctor = fields.Many2one('doctor.info.model')
    patient = fields.Many2one('odoo.clinic.patient')
    visit_id = fields.Char(string="Visit ID", help="Auto Increment")
    visit_count = fields.Integer(string="Visit Count", help="To Display The Count Visits in The Clinic ")
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    patient_class = fields.Char(string="Patient class", required='true')
    # patient_name = fields.related('patient', 'name', type='char', string='Patient Name')
    name = fields.Integer(string="Set ID")
    # change the name of this field to can display it as default when create visit
    assigned_patient_location = fields.Text(string="Assigned Location")
    admission_type = fields.Char(string="Admission Type")
    preadmit_number = fields.Integer(string="Preadmit Number")
    prior_patient_location = fields.Text(string="Prior Location")
    attending_doctor = fields.Selection([('value', 'No suggested values defined')], string="Attending Doctor")
    referring_doctor = fields.Selection([('value', 'No suggested values defined')], string="Referring Doctor")
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
    admitting_doctor = fields.Selection([('value', 'No suggested values defined')], string="Admitting Doctor")
    patient_type = fields.Selection([('value', 'No suggested values defined')])
    visit_number = fields.Integer(string="Visit Number",
                                  help="This field contains the unique number assigned to each patient visit.")
    # This field contains the unique number assigned to each patient visit.
    financial_class = fields.Selection([('value', 'No suggested values defined')], string="Financial Class")
    # This field contains the financial class(es) assigned to the patient for the purpose of identifying
    # sources of reimbursement
    charge_price_indicator = fields.Selection([('value', 'No suggested values defined')], string="Charge Price Code")
    # This field contains the code used to determine which price schedule is to be used for room and bed charges.
    courtesy_code = fields.Selection([('value', 'No suggested values defined')], string="Courtesy Code")
    credit_rating = fields.Selection([('value', 'No suggested values defined')], string="Credit Rating")
    # This field contains the user-defined code to determine past credit experience
    contract_code = fields.Selection([('value', 'No suggested values defined')], string="Contract Code")
    # This field identifies the type of contract entered into by the health care facility and the guarantor
    # for the purpose of settling outstanding account balances.
    contract_effective_date = fields.Date(string="Contract Date")
    # This field contains the date that the contract is to start or started.
    contract_amount = fields.Integer(string="Contract Amount")
    # This field contains the amount to be paid by the guarantor each period according to the
    # contract.
    contract_period = fields.Integer(string="Contract Period")
    # This field contains the amount to be paid by the guarantor each period according to the
    # contract.
    interest_code = fields.Selection([('value', 'No suggested values defined')], string="Interest Amount")
    # This field indicates the amount of interest that will be charged
    transfer_bad_debt_code = fields.Selection([('value', 'No suggested values defined')], string="Bad Debt Code")
    # This field indicates that the account was transferred to bad debts and gives the reason.
    transfer_bad_debt_date = fields.Date(string="Bad Debt Date")
    # This field contains the date that the account was transferred to a bad debt status.
    bad_debt_agency_code = fields.Integer(string="Bad Debt Agency Code")

    bad_debt_transfer_amount = fields.Integer(string="Amount of Bad Debt Transfer")
    bad_debt_recovery_amount = fields.Integer(string="Amount of Bad Debt Recovery")
    delete_account_indicator = fields.Selection([('value', 'No suggested values defined')],
                                                string="Delete Account Indicator")
    delete_account_indicator_reasons = fields.Text(string="Reasons Of Delete Account")
    # This field indicates that the account was deleted from the file and gives the reason
    delete_account_date = fields.Date(string="Delete Account Date")
    discharge_disposition = fields.Selection([('value', 'No suggested values defined')], string="Discharge Disposition")
    discharged_location = fields.Text(string="Discharged Location")
    # This field indicates the health care facility to which the patient was discharged and the date.
    diet_type = fields.Selection([('value', 'No suggested values defined')])
    servicing_facility = fields.Selection([('value', 'No suggested values defined')], string="Servicing Facility")
    account_status = fields.Selection([('value', 'No suggested values defined')], string="Account Status")
    pending_location = fields.Text(string="Pending Location")
    admit_date = fields.Datetime(string="Admit Date/Time")
    discharge_date = fields.Datetime(string="Discharge Date/Time")
    current_patient_balance = fields.Char(string="Current Balance")
    # This field contains the visit balance due.
    total_charges = fields.Integer(string="Total Visit Charges")
    total_adjustments = fields.Integer(string="Total Adjustments")
    total_payments = fields.Integer(string="Total Payment")
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
    @api.model
    def create(self, vals):
        # print(vals['visit_count'])
        vals['visit_id'] = self.env['ir.sequence'].next_by_code('clinic.visit')
        # records = self.env['visit.model'].sudo().search([])
        # print(records)
        # vals['visit_count'] = len(records)
        # print(vals['visit_count'])
        res = super(Visit, self).create(vals)
        return res
