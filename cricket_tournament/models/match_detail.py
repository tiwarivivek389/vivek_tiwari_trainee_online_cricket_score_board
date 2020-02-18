# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class MatchDetail(models.Model):
    _name = "match.detail"
    _description = "Match Detail"

    name = fields.Char(string="Match Name", required=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    team1name_id = fields.Many2one("team.detail", string="Team1Name")
    team2name_id = fields.Many2one("team.detail", string="Team2Name")
    matchover = fields.Char(string="Match Over")
    matchdatetime = fields.Datetime(string="Match_Date_Time")
    umpirename = fields.Char(string="Umpire Name")
    matchvenue = fields.Text(string="Match Venue")
    match_id = fields.Many2one("tournament.detail", string="match", ondelete="restrict")
