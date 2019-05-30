from odoo import models, fields, api

class Visit(models.Model):
    _name = 'odoo.clinic.visit'

    patient_class=fields.Char(string="Patient class",required ='true')
    set_id = fields.Integer(string="Set ID")
    assigned_patient_location = fields.Text(string="Assigned Location")
    admission_type = fields.Char(string="Admission Type")
    preadmit_number = fields.Integer(string="Preadmit Number")
    prior_patient_location = fields.Text(string="Prior Location")
    # attending_doctor=
    # referring_doctor=
    # hospital_service=
    temporary_location = fields.Char(string="Temporary Location")
    prior_temporary_location = fields.Text(string="Previous Temporary Location")
    preadmit_test_indicator = fields.Char(string="Preadmit Test Indicator")
    re_admission_indicator = fields.Char(string="Re-Admission Indicator")
    admit_source = fields.Char(string="Admit Source")
    ambulatory_status = fields.Char(string="Ambulatory Status")
    vip_indicator = fields.Char(string="VIP-Type")
    admitting_doctor = fields.Char(string="Admitting Doctor")
    patient_type = fields.Char()
    visit_number = fields.Integer(string="Visit Number")
    # This field contains the unique number assigned to each patient visit.
    financial_class = fields.Char(string="Financial Class")
    # This field contains the financial class(es) assigned to the patient for the purpose of identifying
    # sources of reimbursement
    charge_price_indicator = fields.Integer(string="Charge Price Code")
    # This field contains the code used to determine which price schedule is to be used for room and bed charges.
    courtesy_code = fields.Integer(string="Courtesy Code")
    credit_rating = fields.Integer(string="Credit Rating")
    # This field contains the user-defined code to determine past credit experience
    contract_code = fields.Selection([('value', 'No suggested values defined')], string="Contract Code")
    # This field identifies the type of contract entered into by the health care facility and the guarantor
    # for the purpose of settling outstanding account balances.
    contract_effective_Date = fields.Date(string="Contract Date")
    # This field contains the date that the contract is to start or started.
    contract_amount = fields.Integer(string="Contract Amount")
    # This field contains the amount to be paid by the guarantor each period according to the
    # contract.
    Contract_Period = fields.Integer(string="Contract Period")
    # This field contains the amount to be paid by the guarantor each period according to the
    # contract.
    interest_code = fields.Integer(string="Interest Amount")
    # This field indicates the amount of interest that will be charged
    transfer_bad_debt_code = fields.Selection([('value', 'No suggested values defined')], string="Bad Debt Code")
    # This field indicates that the account was transferred to bad debts and gives the reason.
    transfer_bad_debt_date = fields.Date(string="Bad Debt Date")
    # This field contains the date that the account was transferred to a bad debt status.
    bad_debt_agency_code = fields.Integer(string="Bad Debt Agency Code")

    bad_debt_transfer_amount = fields.Integer(string="Amount of Bad Debt Transfer")
    bad_debt_recovery_amount = fields.Integer(string="Amount of Bad Debt Recovery")
    delete_account_indicator = fields.Selection([[('value', 'No suggested values defined')]], string="Delete Account Indicator")
    # This field indicates that the account was deleted from the file and gives the reason
    delete_account_date = fields.Date(string="Delete Account Date")
    discharge_disposition = fields.Char(string="Discharge Disposition")
    discharged_location = fields.Char(string="Discharged Location")
    # This field indicates the health care facility to which the patient was discharged and the date.
    diet_type = fields.Selection([('value', 'No suggested values defined')])
    servicing_facility = fields.Selection([('value', 'No suggested values defined')], string="Servicing Facility")
    account_status = fields.Selection([('value', 'No suggested values defined')], string="Account Status")
    pending_location = fields.Text(string="Pending Location")
    prior_temporary_location=fields.Char()
    admit_date=fields.Date()
    discharge_date=fields.Date()
    current_patient_balance=fields.Char()
    total_charges=fields.Integer()
    Total_Adjustments=fields.Integer()
    total_payments=fields.Integer()
    alternate_visit_id=fields.Integer()
    visit_indicator=fields.Integer()
    # Other Healthcare Provider
    service_episode_description=fields.Text()
    service_episode_identifier=fields.Integer()