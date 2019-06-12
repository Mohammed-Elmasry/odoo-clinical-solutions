# _*_ coding: utf-8 _*_

from odoo import models, fields

class Product (models.Model):
    _inherit = "product.template"
    _description = "resources, products, and services offered by the clinic"
    _order = "date_added desc, name"
    name = fields.Char('Name',required=True)
    # fees = fields.Monetary('fees', currency_field='currency_id')
    date_added = fields.Date('creation date')

    # categorization (service vs medicine)

    is_medicine = fields.Boolean(string="is medicine")
    # item_identifier = fields.Char(string="item identifier", required=True)
    item_description = fields.Text(string="item description")
    item_status = fields.Selection([("A", "Active"),("P","Pending inactive"),("I","Inactive")])
    item_type = fields.Selection([("EQP", "Equipment"),("SUP","Supply"),("IMP","Implant"),("MED","Medication"),("TDC","Tubes, Drains, and Catheters")])
    item_category = fields.Selection([("L","L"), ("99zzz","99zzz"), ("ACR ALPHAID2006","ACR ALPHAID2006"),
        ("ALPHAID2007","ALPHAID2007"), ("ALPHAID2008","ALPHAID2008"),("ALPHAID2009","ALPHAID2009"),("ALPHAID2010","ALPHAID2010"),
        ("ALPHAID2011","ALPHAID2011")])
    subject_to_expiration_indicator = fields.Selection([("Y","Yes"),("N","No"),("NI","No Information"),("NA","Not applicable")])

    # manufacturer information
    #done in xml
    manufacturer_identifier = fields.Char(string="manufacturer identifier")
    manufacturer_name = fields.Char(string="manufacturer name")
    manufacturer_catalog_number = fields.Float(string="manufacturer catalog number")
    manufacturer_labeler_identification_code = fields.Float(string="manufacturer labeler identification code")

    # monetary information
    #done in xml
    patient_chargeable_indicator = fields.Selection([("Y","Yes"),("N","No"),("NI","No Information"),("NA","Not applicable")])
    transaction_code = fields.Selection([("NS","No suggested code value")])
    transaction_amount = fields.Monetary(string="transaction amount (money paid)")

    # stock and supply info

    stock_item_indicator = fields.Selection([("Y","Yes"),("N","No"),("NI","No Information"),("NA","Not applicable")])
    supply_risk_codes = fields.Selection([("COR","Corrosive"),("FLA","Flammable"),("EXP","Explosive"),("INJ","Injury hazard")])
    approving_regulator_agency = fields.Selection([("FDA","Food and drug Administration"),("AMA","American Medical Association")])
    latex_indicator = fields.Selection([("Y","Yes"),("N","No"),("NI","No Information"),("NA","Not applicable")])