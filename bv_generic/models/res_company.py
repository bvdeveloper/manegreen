# -*- coding: utf-8 -*-
from odoo import _, api, models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    company_stamp = fields.Binary(string="Company Stamp", groups="base.group_system")
