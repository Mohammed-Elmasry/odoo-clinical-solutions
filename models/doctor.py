from odoo import fields, models, api


class DoctorInfo(models.Model):
    _name = "doctor.info.model"
    _inherits = {'hr.employee': 'emp_id'}

    emp_id = fields.Many2one('hr.employee')
    doctor_id = fields.Integer(string="Doctor ID", help="Auto Increment Field")
    user_id = fields.Many2one('res.users', related='emp_id.user_id')
    # user_id = fields.Many2one('res.users',compute='calculate_user',store=True)
    user=fields.Integer()
    visit = fields.One2many('visit.model', 'doctor')
    visit_count = fields.Integer(related="visit.visit_count", string="Visit Count")
    role = fields.Selection([("doctor", "Doctor"), ("officer", "Officer"), ("nurse", "Nurse")], required=True
                            , help="Employee's Role in Our Clinic")
    services_and_products = fields.Many2one('product.template')
    speciality = fields.Selection([
        ('registrar', 'Registrar Doctor'),
        ('consultant', 'Consultant Doctor'),
        ('intern', 'Intern Doctor'),
        ('fellowship', 'Fellowship Doctor'),
        ('resident', 'Resident Doctor')])
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

    # @api.depends('emp_id')
    def calculate_user(self):
        # self.env['res.users'].create({"id":self.emp_id.user_id})
        # self.env['user_id']=self.emp_id.user_id
        self.user_id=self.emp_id.user_id
        print(self.emp_id.user_id)

    #
    # @api.model
    # def create(self, vals):
        # vals['doctor_id'] = self.env['ir.sequence'].next_by_code('clinic.employee')
        # vals = {"id":self.emp_id.user_id}
        # return super(res.users, self).create(vals)
            # print(emp_id)

    @api.model
    def create(self, vals):
        # model_res_users = self.env['res_users'].create({'id':self.user_id})
        # print(self.emp_id.user_id)
        # vals['user_id']= self.env['res.users'].search(args=[('id', '=', self.emp_id.user_id.id)])
        # vals['user_id']="13"

        # print(vals['user_id'])
        return super(DoctorInfo, self).create(vals)