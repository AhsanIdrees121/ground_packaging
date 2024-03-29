# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _get_combination_info(
        self,
        combination=False,
        product_id=False,
        add_qty=1,
        parent_combination=False,
        only_template=False,
    ):
        template = self.with_context(website_sale_stock_available=True)
        return super(ProductTemplate, template)._get_combination_info(
            combination,
            product_id,
            add_qty,
            parent_combination,
            only_template,
        )
