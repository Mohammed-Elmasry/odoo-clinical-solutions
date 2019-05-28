from odoo import models, fields, api

class Visit(models.Model):
    _name = 'odoo.clinic.visit'

    patient_class=fields.Char(string="Patient class",required ='true')
    set_id = fields.Integer(string="Set ID")
    assigned_patient_location = fields.Char(string="Assigned Patient Location")
    admission_type=fields.Char()
    preadmit_number=fields.Integer()
    prior_patient_location=fields.Char()
    # attending_doctor=
    # referring_doctor=
    # hospital_service=
    temporary_location=fields.Char()
    preadmit_test_indicator=fields.Char()
    re_admission_indicator=fields.Char()
    admit_source=fields.Char()
    ambulatory_status=fields.Char()
    vip_indicator=fields.Char()
    admitting_doctor=fields.Char()
    patient_type=fields.Char()
    visit_number=fields.Integer()
    financial_class=fields.Char()
    charge_price_indicator=fields.Integer()
    courtesy_code=fields.Integer()
    credit_rating=fields.Integer()
    contract_code=fields.Integer()
    contract_effective_Date=fields.Date()
    contract_amount=fields.Integer()
    Contract_Period=fields.Integer()
    interest_code=fields.Integer()
    transfer_bad_debt_code=fields.Integer
    transfer_bad_debt_date=fields.Date()
    bad_debt_agency_code=fields.Integer()

    bad_debt_transfer_amount=fields.Integer()
    bad_debt_recovery_amount=fields.Integer()
    delete_account_indicator=fields.Integer()
    delete_account_date=fields.Date()
    discharge_disposition=fields.Char()
    discharged_location=fields.Char()
    diet_type=fields.Char()
    servicing_facility=fields.Char()
    # Bed Status
    account_status=fields.Char()
    pending_location=fields.Char()
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