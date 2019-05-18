# _*_ coding: utf-8 _*_

from odoo import models, fields

class Product (models.Model):
    _name = 'clinical_management_system.product' #identifier
    _description = "resources, products, and services offered by the clinic"
    _order = "date_added desc, name"
    name = fields.Char('Description',required=True)
    fees = fields.Float()
    date_added = fields.Date('creation date')
