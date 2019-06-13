from odoo import models, fields, api

class Medical(models.Model):
    _name = 'odoo.clinic.medical'



    obstetric_gynecological_history = fields.Text()
    dm = fields.Boolean()
    htn = fields.Boolean()
    cardiac = fields.Boolean()
    heptic = fields.Boolean()
    renal = fields.Boolean()
    others = fields.Text()

    surgical_history = fields.Text()
    bp = fields.Float()
    rr = fields.Float()
    hr = fields.Float()
    temp = fields.Float()
    fhc = fields.Float()
    weight = fields.Float()
    obese = fields.Boolean()
    average_weight = fields.Boolean()
    under_weight = fields.Boolean()
    examination = fields.Text()
    drug_allergy = fields.Text()
    # physician_signature=
    date = fields.Date()
    time = fields.Datetime()
    patient=fields.Many2one('odoo.clinic.patient')
    doctor=fields.Many2one('doctor.info.model')
    visit=fields.Many2one('visit.model')