from odoo import fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
import pytz


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    def _create_date_range_seq(self, date):
        # Fix issue creating new date range for future dates
        # It assigns more than one month
        # TODO: Remove if odoo merge the following PR:
        # https://github.com/odoo/odoo/pull/91019
        date_obj = fields.Date.from_string(date)
        sequence_range = self.env["ir.sequence.date_range"]
        prefix_suffix = "%s %s" % (self.prefix, self.suffix)
        if "%(range_day)s" in prefix_suffix:
            date_from = date_obj
            date_to = date_obj
        elif "%(range_month)s" in prefix_suffix:
            date_from = fields.Date.start_of(date_obj, "month")
            date_to = fields.Date.end_of(date_obj, "month")
        else:
            date_from = fields.Date.start_of(date_obj, "year")
            date_to = fields.Date.end_of(date_obj, "year")
        date_range = sequence_range.search(
            [
                ("sequence_id", "=", self.id),
                ("date_from", ">=", date),
                ("date_from", "<=", date_to),
            ],
            order="date_from desc",
            limit=1,
        )
        if date_range:
            date_to = fields.Date.subtract(date_range.date_from, days=1)
        date_range = sequence_range.search(
            [
                ("sequence_id", "=", self.id),
                ("date_to", ">=", date_from),
                ("date_to", "<=", date),
            ],
            order="date_to desc",
            limit=1,
        )
        if date_range:
            date_to = fields.Date.add(date_range.date_to, days=1)
        sequence_range_vals = {
            "date_from": date_from,
            "date_to": date_to,
            "sequence_id": self.id,
        }
        seq_date_range = sequence_range.sudo().create(sequence_range_vals)
        return seq_date_range

    def _get_prefix_suffix(self, date=None, date_range=None):
        def _interpolate(s, d):
            return (s % d) if s else ''

        def _interpolation_dict():
            now = range_date = effective_date = datetime.now(pytz.timezone(self._context.get('tz') or 'UTC'))
            if date or self._context.get('ir_sequence_date'):
                effective_date = fields.Datetime.from_string(date or self._context.get('ir_sequence_date'))
            if date_range or self._context.get('ir_sequence_date_range'):
                range_date = fields.Datetime.from_string(date_range or self._context.get('ir_sequence_date_range'))

            sequences = {
                'year': '%Y', 'month': '%m', 'day': '%d', 'y': '%y', 'doy': '%j', 'woy': '%W',
                'weekday': '%w', 'h24': '%H', 'h12': '%I', 'min': '%M', 'sec': '%S'
            }
            if (
                       self._context.get('model_name') == 'account.move' and
                       self._context.get('ir_sequence_date')
            ):
                fy = str(range_date.year)[2:] + '-' + str(range_date.year + 1)[2:]
                sequences.update({'fy': fy})
            res = {}
            for key, format in sequences.items():
                res[key] = effective_date.strftime(format)
                res['range_' + key] = range_date.strftime(format)
                res['current_' + key] = now.strftime(format)

            return res

        self.ensure_one()
        d = _interpolation_dict()
        try:
            interpolated_prefix = _interpolate(self.prefix, d)
            interpolated_suffix = _interpolate(self.suffix, d)
        except ValueError:
            raise UserError(_('Invalid prefix or suffix for sequence \'%s\'') % self.name)
        return interpolated_prefix, interpolated_suffix
