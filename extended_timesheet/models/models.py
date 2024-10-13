# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
	_inherit = 'account.analytic.line'

	coche_personal = fields.Boolean(string="Personal car?")
	kilometros = fields.Integer(string="Kilometres")
	lugar = fields.Char(string="Mission place")
	servicio_campo = fields.Integer(string="Lunches")
