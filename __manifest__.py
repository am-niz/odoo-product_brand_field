# -*- coding: utf-8 -*-
{
    'name': "Product Brand",

    'summary': "Product Brand Details",

    'description': """
Long description of module's purpose
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
        'views/order_line_product_brand.xml',
        'views/inventory_line_product_brand_views.xml',
    ],
}

