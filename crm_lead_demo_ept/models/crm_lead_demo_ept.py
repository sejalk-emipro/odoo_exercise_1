# -*- coding :utf-8 -*-

from openerp import models,fields

class CRMLead(models.Model):

    _name="crm.lead.demo.ept"
    _description="Customer relationship management Lead"

    name=fields.Char(string="Customer Name",help="Name of the customer",required=True)
    email=fields.Char(string="Customer Email",help="Email of the customer",required=True)
    phone=fields.Char(string="Customer Phone",help="Phone no. of the customer",required=True)
    expected_revenue=fields.Float(string="Expected Revenue",digits=(16,2),help="Expected revenue of the company")
    salesperson=fields.Char(string="Sales Person",help="Name of the sales person",required=True)
    sales_team=fields.Char(string="Sales Team")
    campaign=fields.Char(string="Campaign")
    channel=fields.Selection([('Facebook','Facebook'),('WhatsApp','WhatsApp'),('Email','Email'),('Newspaper','Newspaper')
                              ,('Television','Television'),('Phone Call','Phone Call'),
                              ('SMS','SMS'),('Google Ads','Google Ads')], string="Channel",required=True)
    state=fields.Selection([('New','New'),('Qualified','Qualified'),('Proposition','Proposition'),
                            ('Won','Won'),('Lost','Lost')], string="State", default="New")
    next_follow_date=fields.Date(string="Next Follow Up Date",required=True)
    won_date=fields.Date(string="Won Date")
    lost_reason=fields.Text(string="Lost Reason",help="Add lost reason")