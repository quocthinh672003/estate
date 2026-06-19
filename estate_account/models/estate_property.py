from odoo import Command, models


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        res = super().action_sold()
        
        for property_recordq in self:
            self.env["account.move"].create({
                "partner_id": property_recordq.buyer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    Command.create({
                        "name": "Selling Price Commission",
                        "quantity": 1,
                        "price_unit": property_recordq.selling_price * 0.06,
                    }),
                    Command.create({
                        "name": "Administration Fees",
                        "quantity": 1,
                        "price_unit": 100.00,
                    })
                ]
            })
        return res