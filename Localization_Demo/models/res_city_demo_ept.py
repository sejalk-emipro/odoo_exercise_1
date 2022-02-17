# -*- coding :utf-8 -*-

from openerp import models,fields

class City(models.Model):

    _name="res.city.demo.ept"
    _description="City Data"

    name=fields.Char(string="City Name")
    state=fields.Char(string="State Name",copy=False)
    active = fields.Boolean(string="Active", default=True)