# -*- coding :utf-8 -*-

from openerp import models,fields

class Country(models.Model):

    _name="res.country.demo.ept"
    _description="Country Data"

    name=fields.Char(string="Country Name" ,help="Enter Country Name")
    code=fields.Char(string="Country Code",help="Enter Country Code")
    active=fields.Boolean(string="Active",default=True)