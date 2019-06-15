from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherits = {'hr.employee': 'emp_id'}

    emp_id = fields.Many2one('hr.employee')
    doctor_id = fields.Integer(string="Doctor ID", help="Auto Increment Field")
    visit = fields.One2many('visit.model', 'doctor')
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True
                            , help="Employee's Role in Our Clinic")
    services_and_products = fields.Many2one('product.template')
    speciality = fields.Char(size=50)
    license_id = fields.Char(size=14, string="License ID", help="Licence ID Related to Employee in Our Clinic")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", default="male", required=True, help="Gender Related to Employee In The Clinic ")
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
    sheet = fields.One2many('odoo.clinic.medical', 'doctor')
