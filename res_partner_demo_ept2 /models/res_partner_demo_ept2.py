# -*- coding: UTC-8 -*-

from openerp import models,fields

class PartnerDemo2(models.Models):
    _name="res.partner.demo.ept2"
    _description="Partner Demo2"

    name = fields.Char(string="Name", help="Customer name")
    email = fields.Char(string="Email")
    street1 = fields.Char(string="Street1")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    zip_code = fields.Char(string="ZipCode")
    country = fields.Char(string="Country")
    birthdate = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age")
    weight = fields.Float(string="Weight")
    description = fields.Text(string="Description")
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], string="Gender",
                              default="Male")
    details = fields.Html(string="Details", help='Add additional details of the customer')
    is_spectacles = fields.Boolean(string="Is Spectacle")
    photo = fields.Binary(string="Image")