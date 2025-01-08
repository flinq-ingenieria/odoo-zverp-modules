from odoo import models, fields, api

class Matricula(models.Model):
    _name = 'res.partner.matricula'
    _description = 'Matrícula'

    name = fields.Char(string='Matrícula', required=True)
    partner_id = fields.Many2one('res.partner', string='Propietario', ondelete='cascade')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    matricula_ids = fields.One2many(
        'res.partner.matricula', 'partner_id', string='Matrículas'
    )


class AccountMove(models.Model):
    _inherit = 'account.move'

    matricula_id = fields.Many2one('res.partner.matricula', string='Matrícula')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id and self.partner_id.matricula_ids:
            self.matricula_id = self.partner_id.matricula_ids[0]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    matricula_id = fields.Many2one('res.partner.matricula', string='Matrícula')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id and self.partner_id.matricula_ids:
            self.matricula_id = self.partner_id.matricula_ids[0]
