# -*- coding :utf-8 -*-

from openerp import models,fields

class StateDemo(models.Model):

    _name="res.state.demo.ept"
    _description="State Details"

    name=fields.Char(string="State Name", help="Enter the state name")
    code=fields.Char(string="State Code",help="Enter the short code of the state")
    country=fields.Char(string="Country Name" ,help="Enter the country name",copy=False)
    active=fields.Boolean(string="Active",default=True)