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
    # item_identifier = fields.Char(string="item identifier", required=True)
    item_description = fields.Text(string="item description")
    item_status = fields.Selection([("A", "Active"),("P","Pending inactive"),("I","Inactive")])
    item_type = fields.Selection([("EQP", "Equipment"),("SUP","Supply"),("IMP","Implant"),("MED","Medication"),("TDC","Tubes, Drains, and Catheters")])
    item_category = fields.Selection([("L","L"), ("99zzz","99zzz"), ("ACR ALPHAID2006","ACR ALPHAID2006"),
        ("ALPHAID2007","ALPHAID2007"), ("ALPHAID2008","ALPHAID2008"),("ALPHAID2009","ALPHAID2009"),("ALPHAID2010","ALPHAID2010"),
        ("ALPHAID2011","ALPHAID2011")])