from odoo import models, fields, api

class Patient(models.Model):
    _name = 'odoo.clinic.patient'
    _inherit = 'res.partner'


    mrn = fields.Char()
    blood_group= fields.Char()
    height= fields.Float()
    weight= fields.Float()

    religion=fields.Char()
    set_id=fields.Integer()
    # sex=fields.Selection((('m','male'),('f','female')))
    # MaritalStatus=fields.selection(['singel','single'],[''])
    mother_name=fields.Char()
    # list of tuple
    # Primary_Language=fields.Selection((('a','Arabic'),('e','English')))
    # Marital_Status=fields.Selection((('s','Single'),('m','Married'),))
    birth_place=fields.Char()
    birth_order=fields.Char()
    patient_account_number=fields.Integer()
    patient_death=fields.Datetime()
    patient_death_indicator=fields.Char()
    multiple_birth_indicator=fields.Char()
    # medical_sheet=fields.one2many('odoo.clinic.medical')
    visit=fields.One2many('odoo.clinic.visit','patient')
    medical=fields.One2many('odoo.clinic.medical','patient')
    # doctor=fields.One2many('odoo.clinic.medical','patient')
