# -*- coding: utf-8 -*-
from odoo import _, api, models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    company_stamp = fields.Binary(string="Company Stamp", groups="base.group_system")
    factory_address = fields.Text()
    factory_pan_number = fields.Char(string="PAN Number")
    # Company Bank Details
    bank_account_name = fields.Char(string="Account Name")
    bank_name = fields.Char(string="Bank Name")
    bank_ifsc_code = fields.Char(string="IFSC Code")
    bank_branch = fields.Char(string="Branch")
    bank_branch_address = fields.Text(string="Branch Address")


