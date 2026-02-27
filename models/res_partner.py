from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # The field that will store the debt calculation
    net_balance = fields.Monetary(
        string="Net Balance", 
        compute="_compute_net_balance",
        currency_field='currency_id'
    )

    @api.depends('credit', 'debit')
    def _compute_net_balance(self):
        for partner in self:
            # Credit (They owe you) - Debit (You owe them)
            # Result: Positive for customers, Negative for vendors you owe.
            partner.net_balance = partner.credit - partner.debit
