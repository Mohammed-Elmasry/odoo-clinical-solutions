# _*_ coding: utf-8 _*_

from odoo import models, fields

class Product (models.Model):
    _name = 'clinical_management_system.product' #identifier
    _inherit = "product.template"
    _description = "resources, products, and services offered by the clinic"
    _order = "date_added desc, name"
    name = fields.Char('Description',required=True)
    fees = fields.Monetary('fees', currency_field='currency_id')
    currency_id = fields.Many2one('res_currency', string="Currency")
    date_added = fields.Date('creation date')
