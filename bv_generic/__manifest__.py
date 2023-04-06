# -*- coding: utf-8 -*-
{
    'name': "BV Generic Customization",
    'summary': "Generic Customization",
    'description': """
                Generic Customization
                - 
            """,

    'author': 'Brainvire',
    'website': 'https://www.brainvire.com/',
    'category': 'Order Modules',
    'version': '16.0.0',
    'depends': ['base', 'web', 'stock', 'stock_barcode', 'product', 'purchase', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/report_invoice.xml',
        'views/account_move_view.xml',
    ],

    'license': 'LGPL-3',
    'auto_install': False,
    'application': False
}
