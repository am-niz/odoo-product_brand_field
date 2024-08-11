# -*- coding: utf-8 -*-
{
    'name': "Product Brand",

    'summary': "Product Brand Details and product brand added to order line and inventory line",

    'description': """
Product Brand Details and product brand added to order line and inventory line
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'account', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand.xml',
        'views/product_template_product_brand_views.xml',
        'views/stock_purchase_sale_menu_views.xml',
        'views/purchase_order_line_views.xml',
        'views/sale_order_line_views.xml',
        'views/stock_order_line_views.xml',
        'views/invoice_order_line_views.xml',
    ],
    'application': True,
    'sequence': -96,
}

