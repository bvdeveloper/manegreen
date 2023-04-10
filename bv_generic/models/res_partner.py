from odoo import api, fields, models, _, Command


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pan_card = fields.Char(string="PAN card")
