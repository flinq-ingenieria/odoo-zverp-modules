from odoo import models, fields, api
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'

    seniority_date = fields.Date(string="Seniority Date", default=lambda self: date.today() if not self.id else False)
    seniority_years = fields.Integer(string="Seniority (Years)", compute='_compute_seniority_years', store=True)

    @api.depends('seniority_date')
    def _compute_seniority_years(self):
        for partner in self:
            if partner.seniority_date:
                today = date.today()
                seniority_date = partner.seniority_date
                partner.seniority_years = today.year - seniority_date.year - ((today.month, today.day) < (seniority_date.month, seniority_date.day))
            else:
                partner.seniority_years = 0

    @api.model
    def create(self, vals):
        if 'seniority_date' not in vals:
            vals['seniority_date'] = date.today()
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'seniority_date' not in vals:
            vals['seniority_date'] = self.seniority_date
        return super(ResPartner, self).write(vals)
