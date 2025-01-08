# -*- coding: utf-8 -*-
{
    'name': "partner_matriculas",

    'summary': """Modulo básico para facturacion taller de coches""",

    'description': """
	Modulo básico para facturacion taller de coches
    """,

    'author': "zvERP",
    'website': "https://www.zverp.com",
    'license': "AGPL-3",

    'category': 'Uncategorized',
    'version': '15.0.1.0',

    'depends': ['base', 'sale_management', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
