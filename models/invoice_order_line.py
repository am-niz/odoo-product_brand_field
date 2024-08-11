from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move.line"

    product_brand = fields.Many2one(
        "product.brand",
        related="product_id.product_tmpl_id.product_brand_id"
    )