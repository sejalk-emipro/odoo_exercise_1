#-*- coding :utf-8 -*-
{
    'name':'Employee',
    'category':'Utility',
    'version':'1.1',
    'author':'Emipro Technology Pvt. Ltd',
    'description':"""
    This module demonstration of the employee data
    """,
    'website':'https://www.emiprotechnologies.com',
    'depends':['sales_team'],
    'data':['security/employee_security.xml',
            'security/ir.model.access.csv',
            'views/employee_demo_ept.xml'],
    'demo':[],
    'sequence':13,
    'auto_install':False,
    'application':False,
    'installable':True,
}