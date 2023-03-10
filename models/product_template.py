from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    grade = fields.Selection([
        ('best', 'Best'),
        ('good', 'Good'),
        ('average', 'Average')], string="Grade", default='good')
