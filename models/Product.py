# _*_ coding: utf-8 _*_

from odoo import models, fields

class Product (models.Model):
    _name = 'clinical_management_system.product' #identifier
    name = fields.Char('Description',required=True)
    fees = fields.Float()
