from odoo import fields, models

class Doctor_info(models.Model):
    _name = "doctor.info.model"
    _inherit = 'hr.employee'
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True)
    speciality = fields.Char(size=50)
