from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherit = 'hr.employee'
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True)
    speciality = fields.Char(size=50)
    personal_phone = fields.Text('Phone Number', size=25)
