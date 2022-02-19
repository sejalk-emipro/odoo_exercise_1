# -*- coding :uft-8 -*-

from openerp import models,fields

class EmployeeData(models.Model):

    _name="employee.demo.ept"
    _description="Employee Data"

    name=fields.Char(string="Employee Name", help="Name of the employee")
    department=fields.Char(string="Department",help="Department name of the employee")
    position=fields.Char(string="Job Position")
    salary=fields.Float(string="Salary",digits=(6,2))
    hire_date=fields.Date(string="Hire Date")
    gender=fields.Selection([('Male','Male'),('Female','Female'),('Transgender','Transgender')], string="Gender")
    job_type=fields.Selection([('Permanent','Permanent'),('Adhoc','Adhoc')], string="Job Type")