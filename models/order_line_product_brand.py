from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand_id = fields.Many2one(
        'product.brand',
        string='Product Brand',
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.product_brand_id = self.product_id.product_tmpl_id.product_brand_id
        else:
            self.product_brand_id = False













    # from odoo import models, fields, api
    #
    #
    # class SaleOrderLine(models.Model):
    #     _inherit = 'sale.order.line'
    #
    #     product_brand_id = fields.Many2one(
    #         'product.brand',
    #         string='Product Brand',
    #         related='product_id.product_tmpl_id.product_brand_id',
    #         # store=True,
    #         readonly=True
    #     )

    # from odoo import models, fields, api
    #
    #
    # class SaleOrderLine(models.Model):
    #     _inherit = 'sale.order.line'
    #
    #     product_brand_id = fields.Many2one(
    #         'product.brand',
    #         string='Product Brand',
    #         compute='_compute_product_brand',
    #         # store=True,
    #     )
    #
    #     @api.depends('product_id')
    #     def _compute_product_brand(self):
    #         for line in self:
    #             if line.product_id:
    #                 line.product_brand_id = line.product_id.product_tmpl_id.product_brand_id
    #             else:
    #                 line.product_brand_id = False

    # product_brand_description = fields.Many2one(
    #     "product.brand",
    #     string="Brand Description"
    # )


    # @api.onchange("product_id")
    # def _onchange_product_id(self):
    #     if self.product_id:
    #         self.product_brand_description = self.product_id.product_tmpl_id.product_brand_id.product_brand_description
    #     else:
    #         self.product_brand_description = False
