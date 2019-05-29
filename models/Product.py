# _*_ coding: utf-8 _*_

from odoo import models, fields

class Product (models.Model):
    _inherit = "product.template"
    _description = "resources, products, and services offered by the clinic"
    _order = "date_added desc, name"
    # name = fields.Char('Name',required=True)
    # fees = fields.Monetary('fees', currency_field='currency_id')
    date_added = fields.Date('creation date')
    is_medicine = fields.Boolean()
