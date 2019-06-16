from odoo import models, fields, api
from odoo import http

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
    # current_user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)

    visit=fields.Many2one('visit.model')
    # @api.onchange('bp')
    # def on_change_state(self):
    #     # record=self.env['doctor.info.model'].search(args=[('user_id', '=', self.env.user)])
    #     print (self.visit.doctor.name)
 
    # add cal
    # @api.depends('time')
    # def calculate_doctor(self):
    #     # self.env['res.users'].create({"id":self.emp_id.user_id})
    #     # self.env['user_id']=self.emp_id.user_id
    #     record1 = self.env['doctor.info.model'].search(args=[('user_id', '=',self._uid)])
    #     print(type(self._uid))
    #     self.doctor=record1.id
    #     print("dsds",self.doctor)
    #
    # @api.model
    # def create(self):
    #     self.env['odoo.clinic.medical'].