from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"

    product_brand_id = fields.Many2one("product.brand",
                                       related="product_id.product_tmpl_id.product_brand_id",
                                       string="Product Brand"
                                       )
