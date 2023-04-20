from odoo import http, models, fields, _, tools, api
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    vehicle_number = fields.Char()
    po_number = fields.Char(string="PO Number")
    comment = fields.Char(string="Narration")
    checked_by = fields.Many2one('res.users', required=False)
    verified_by = fields.Many2one('res.users', required=False)
    auth_sign = fields.Char()


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    move_comment = fields.Char(string="Narration", related="move_id.comment", store=True)

