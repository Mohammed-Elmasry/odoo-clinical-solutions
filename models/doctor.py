from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherits = {'hr.employee': 'emp_id'}

    emp_id = fields.Many2one('hr.employee')
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True)
    speciality = fields.Char(size=50)
    license_id = fields.Char(size=14, string="License ID")
    # name = fields.Char(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", default="male", required=True)
    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", required=True)
    job_title = fields.Char("Job Title", required=True)
    work_phone = fields.Char('Work Phone', required=True)
    work_email = fields.Char('Work Email', required=True)
    certificate = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('other', 'Other'),
    ], 'Certificate Level', default='master', groups="hr.group_hr_user", required=True)
    mobile_phone = fields.Char('Work Mobile', required=True)
    # visit=fields.One2many()
    # visit=fields.Many2one(odoo.clinic.visit)
    # personal_phone = fields.Char('Phone Number', size=25)
    # personal_address = fields.Text('Address', size=50)

    # @api.model
    # def set_doctor(self):
    #     if self.role == 'Doctor':
    #         raise exceptions.ValidationError()
