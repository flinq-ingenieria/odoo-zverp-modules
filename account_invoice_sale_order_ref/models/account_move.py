from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", compute='_compute_sale_order_id', store=False)

    def _compute_sale_order_id(self):
        for record in self:
            sale_order = self.env['sale.order'].search([('name', '=', record.invoice_origin)], limit=1)
            record.sale_order_id = sale_order.id if sale_order else False
