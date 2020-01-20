from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'ocsb.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    tournament_id = fields.Many2one('tournament.detail',string="Tournament Name", required=True)

