# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    context = fields.Char(
        string="Context Value",
        default={},
        required=True,
        help="Context dictionary as Python expression, empty by default "
        "(Default: {})",
    )

    def _get_context(self):
        # self.ensure_one()
        context = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("report.default.context", "{}")
        )
        # We must transform it to a dictionary
        context = safe_eval(context or "{}")
        report_context = safe_eval(self.context or "{}")
        context.update(report_context)
        context.update(self.env.context)
        return context

    def render(self, res_ids, data=None):
        return super(IrActionsReport, self.with_context(self._get_context())).render(
            res_ids, data=data
        )

    def report_action(self, docids, data=None, config=True):
        return super(
            IrActionsReport, self.with_context(self._get_context())
        ).report_action(docids, data=data, config=config)

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        # Check for reports only available for invoices.
        if self._get_report(report_ref).report_name in ('account.report_invoice_with_payments', 'account.report_invoice'):
            invoices = self.env['account.move'].browse(res_ids)
            if any(x.move_type == 'entry' for x in invoices):
                raise UserError(_("Only invoices could be printed."))

        if self._get_report(report_ref).report_name == 'report_context.transporter_account_invoices':
            data['context'].update({'transporter_account_invoices': 1})
        elif self._get_report(report_ref).report_name == 'report_context.triplicate_account_invoices':
            data['context'].update({'triplicate_account_invoices': 1})
        return super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
