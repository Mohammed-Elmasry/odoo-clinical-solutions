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

    # from odoo import models, fields, api

    # class Sheet(models.Model):
    #     _name = 'odoo.clinic.clinical.sheet'
    #
    #     obstetric_gynecological_history = fields.Text()
    #     DM = fields.Boolean()
    #     HTN = fields.Boolean()
    #     cardiac = fields.Boolean()
    #     heptic = fields.Boolean()
    #     renal = fields.Boolean()
    #     others = fields.Text()
    #     surgical_history = fields.Text()
    #     BP = fields.Float()
    #     RR = fields.Float()
    #     HR = fields.Float()
    #     Temp = fields.Float()
    #     FHC = fields.Float()
    #     Weight = fields.Float()
    #     Obese = fields.Boolean()
    #     Average_weight = fields.Boolean()
    #     Under_weight = fields.Boolean()
    #     Examination = fields.Text()
    #     Drug_Allergy = fields.Text()
    #     # physician_signature=
    #     Date = fields.Date()
    #
    #     time = fields.Datetime()