from odoo import models, fields, api


class Patient(models.Model):
    _name = 'odoo.clinic.patient'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner')
    mrn = fields.Char()
    blood_group = fields.Char()
    height = fields.Float()
    weight = fields.Float()
    religion = fields.Char()
    set_id = fields.Integer()
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')])
    MaritalStatus = fields.Selection(
        [('A', 'Separated'), ('D', 'Divorced'), ('M', 'Married'), ('S', 'Single'), ('W', 'Widowed')])
    mother_name = fields.Char()
    race = fields.Selection([('1002-5', 'American Indian or Alaska Native'),
                             ('2028-9', 'Asian'), ('2054-5', 'Black or African American'),
                             ('2076-8', 'Native Hawaiian or Other Pacific Islander'),
                             ('2106-3', 'White'),
                             ('2131-1', 'Other Race')])
    birth_place = fields.Char()
    birth_order = fields.Char()
    patient_account_number = fields.Integer()
    patient_death = fields.Datetime()
    patient_death_indicator = fields.Char()
    multiple_birth_indicator = fields.Char()
    token = fields.Text()
    password = fields.Char()
    # medical_sheet=fields.one2many('odoo.clinic.medical')
    visit = fields.One2many('visit.model', 'patient')
    medical = fields.One2many('odoo.clinic.medical', 'patient')
    # doctor=fields.One2many('odoo.clinic.medical','patient')