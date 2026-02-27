{
    'name': 'Debt Tracker',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Track customer and vendor debt with negative/positive balances',
    'depends': ['base', 'account', 'purchase'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
