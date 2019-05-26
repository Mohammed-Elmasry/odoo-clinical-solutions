from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherits = {'hr.employee': 'emp_id'}

    emp_id = fields.Many2one('hr.employee')
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True)
    speciality = fields.Char(size=50)
    license_id = fields.Integer(size=40 , string="License ID")
    name = fields.Char(related='resource_id.name', store=True, oldname='name_related', readonly=False, required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", default="male",required=True )
    # personal_phone = fields.Char('Phone Number', size=25)
    # personal_address = fields.Text('Address', size=50)
