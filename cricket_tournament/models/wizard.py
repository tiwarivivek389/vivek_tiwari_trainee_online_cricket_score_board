from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'ocsb.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    session_id = fields.Many2one('tournament.detail',string="Session", required=True)