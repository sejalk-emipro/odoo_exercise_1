# -*- coding :utf-8 -*-

from openerp import models,fields

class ProductData(models.Model):

    _name="product.demo.ept"
    _description="Product Demo"

    name=fields.Char(string="Name",help="Name of the product")
    sku=fields.Char(string="SKU",help="SKU(Stock Keeping Unit) of the product")
    barcode=fields.Char(string="Barcode" ,help="Barcode of the product")
    product_sold=fields.Boolean(string="Sold",help="Can this product be sold")
    product_type=fields.Selection([('Storable','Storable'),('Consumable','Consumable'),('Service','Service')],string="Product Type")
    sale_price=fields.Float(string="Sale Price",digits=(6,2))
    cost_price=fields.Float(string="Cost Price",digit=(6,2))
    active=fields.Boolean(string="Active" ,default=True)
    warehouse=fields.Char(string="Warehouse")
    product_image=fields.Binary(string="Image",help="Product Image")
    website_des=fields.Html(string="Website Description")
    internal_note=fields.Text(string="Internal Note")
