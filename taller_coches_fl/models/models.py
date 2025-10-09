from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    matricula = fields.Char(string='Matrícula')


class AccountMove(models.Model):
    _inherit = 'account.move'

    matricula = fields.Char(string='Matrícula')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id and self.partner_id.matricula:
            self.matricula = self.partner_id.matricula
