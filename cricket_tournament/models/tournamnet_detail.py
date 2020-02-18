# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class TournamentDetail(models.Model):
    _name = "tournament.detail"
    _inherit = ['mail.thread']
    _description = "Tournament Detail"

    name = fields.Char(string="Tournament Name", required=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    place = fields.Char(string="Tournament Place")
    tournamenttype = fields.Selection([('latherballtournament', 'Leather Ball Tournaments'), ('tennisballtournament', 'Tennis Ball Tournaments'), ('underarmstournament', 'Underarms Tournaments'), ('tapeballtournament', 'Tape Ball Tournaments')], string="Tournament Type")
    team = fields.Integer(string="Participate Team")
    starting_date = fields.Date(string="Tournament Starting Date")
    ending_date = fields.Date(string="Tournament Ending Date")
    shedule = fields.One2many("match.detail", "match_id", string="Shedule")

    @api.constrains('starting_date', 'ending_date')
    def check_date(self):
        for rec in self:
            if rec.ending_date < rec.starting_date:
                raise ValidationError(('value must be greater than'))
