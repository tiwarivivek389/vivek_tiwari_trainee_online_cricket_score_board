# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Payment(models.Model):
    _name = "payment.detail"
    _description = "Payment Detail"

    name = fields.Char(string="Payment Receiver Name")
    amount = fields.Integer()
