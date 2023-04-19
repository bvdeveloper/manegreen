from odoo import api, fields, models, tools


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    factory_address = fields.Html()
    factory_pan_number = fields.Html()
