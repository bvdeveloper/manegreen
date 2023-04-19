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
    'depends': [
        'base', 'web', 'stock', 'stock_barcode', 'product', 'purchase', 'account',
        'sign', 'bi_print_journal_entries', 'l10n_in', 'report_context', 'l10n_in_sale',
        'l10n_in_purchase',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/account_move_view.xml',
        'views/report_invoice.xml',
        'views/res_partner.xml',
        'views/res_users_views.xml',
        'views/res_company_views.xml',
        'views/report_purchase_order.xml',
        'views/layouts.xml',
        'views/report_sale_order.xml',
        'report/report_journal_entries_view.xml',
        'report/purchase_order_templates.xml',
    ],

    'license': 'LGPL-3',
    'auto_install': False,
    'application': False
}
