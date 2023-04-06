from odoo import http, models, fields, _, tools, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    vehicle_number = fields.Char()
