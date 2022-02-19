#-*- coding :utf-8 -*-
{
    'name':'crm lead demo',
    'category':'Utility',
    'version':'1.1',
    'author':'Emipro Technology Pvt. Ltd',
    'description':"""
    This module demonstration of the employee data
    """,
    'website':'https://www.emiprotechnologies.com',
    'depends':['sales_team'],
    'data':['security/crm_lead_security.xml',
            'security/ir.model.access.csv',
            'views/crm_lead_demo_ept.xml'],
    'demo':[],
    'sequence':14,
    'auto_install':False,
    'application':False,
    'installable':True,
}