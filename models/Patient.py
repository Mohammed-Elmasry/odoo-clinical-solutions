from odoo import models, fields, api

class Patient(models.Model):
    _name = 'odoo.clinic.patient'
    _inherit = 'res.partner'

    mrn = fields.Char()
    blood_group= fields.Char()
    height= fields.Float()
    weight= fields.Float()
    Religion=fields.Char()
    set_id=fields.Integer()
    # sex=fields.Selection((('m','male'),('f','female')))
    # MaritalStatus=fields.selection(['singel','single'],[''])
    mother_name=fields.Char()
    # list of tuple
    # Primary_Language=fields.Selection((('a','Arabic'),('e','English')))
    # Marital_Status=fields.Selection((('s','Single'),('m','Married'),))
    Birth_Place=fields.Char()
    Birth_Order=fields.Char()
    Patient_Account_Number=fields.Integer()
    Patient_Death=fields.Datetime()
    Patient_Death_Indicator=fields.Char()
    Multiple_Birth_Indicator=fields.Char()
    # medical_sheet=fields.one2many('odoo.clinic.medical')
    visit=fields.one2many('odoo.clinic.visit')

