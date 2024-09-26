# __manifest__.py
{
    'name': 'Account Move Sale Order Link',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Add a link from Account Move to Sale Order',
    'author': 'zvERP',
    'license': 'AGPL-3',
    'website': 'https://www.zverp.com',
    'depends': ['account', 'sale'],
    'data': [
        'views/account_move_form.xml',
    ],
    'installable': True,
    'application': False,
}

