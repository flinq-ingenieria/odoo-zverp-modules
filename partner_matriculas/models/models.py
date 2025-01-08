from odoo import models, fields, api

class Matricula(models.Model):
    _name = 'res.partner.matricula'
    _description = 'Matrícula'

    name = fields.Char(string='Matrícula', required=False)
    partner_id = fields.Many2one('res.partner', string='Propietario', ondelete='cascade')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    matricula_ids = fields.One2many(
        'res.partner.matricula', 'partner_id', string='Matrículas'
    )


class AccountMove(models.Model):
    _inherit = 'account.move'

    matricula_id = fields.Many2one('res.partner.matricula', string='Matrícula', compute='_compute_matricula_id', store=True, readonly=False)

    @api.depends('partner_id', 'partner_id.matricula_ids')
    def _compute_matricula_id(self):
        for record in self:
            if record.partner_id and len(record.partner_id.matricula_ids) == 1:
                record.matricula_id = record.partner_id.matricula_ids[0]
            elif not record.partner_id:
                record.matricula_id = False


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    matricula_id = fields.Many2one('res.partner.matricula', string='Matrícula', compute='_compute_matricula_id', store=True, readonly=False)

    @api.depends('partner_id', 'partner_id.matricula_ids')
    def _compute_matricula_id(self):
        for record in self:
            if record.partner_id and len(record.partner_id.matricula_ids) == 1:
                record.matricula_id = record.partner_id.matricula_ids[0]
            elif not record.partner_id:
                record.matricula_id = False
