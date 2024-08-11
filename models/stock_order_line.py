from odoo import fields, models, api


class StockPickingLine(models.Model):
    _inherit = "stock.move"

    product_brand_id = fields.Many2one(
        'product.brand',
        string='Product Brand',
        related="product_id.product_tmpl_id.product_brand_id",
        # store=True,
    )
#
#     @api.depends('product_id')
#     def _compute_product_brand(self):
#
#         """Here with the help of product_id on the delivery page it will search the product_brand and assign to current
#         product_brand_id on the delivery page"""
#
#         for line in self:
#             if line.product_id:
#                 line.product_brand_id = line.product_id.product_tmpl_id.product_brand_id
#             else:
#                 line.product_brand_id = False
#
#
#
#
#
#
#
#     # product_brand_id = fields.Many2one(
#     #     'product.brand',
#     #     'Product Brand',
#     #     related='product_id.product_tmpl_id.product_brand_id',
#     #     readonly=True
#     # )
#     #
#     # product_brand_id = fields.Many2one(
#     #     'product.brand',
#     #     string='Product Brand'
#     # )
#     #
#     # @api.onchange('product_id')
#     # def _onchange_product_id(self):
#     #     if self.product_id:
#     #         self.product_brand_id = self.product_id.product_tmpl_id.product_brand_id
#     #     else:
#     #         self.product_brand_id = False