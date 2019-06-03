from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherits = {'hr.employee': 'emp_id'}

    emp_id = fields.Many2one('hr.employee')
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True)
    speciality = fields.Char(size=50)
    license_id =fields.Integer()
    # patient=fields.
    # personal_phone = fields.Char('Phone Number', size=25)
    # personal_address = fields.Text('Address', size=50)
