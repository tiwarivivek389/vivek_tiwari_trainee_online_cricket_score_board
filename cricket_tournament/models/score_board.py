# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ScoreBoard(models.Model):
    _name = "score.board"
    _description = "Score Board"

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    over = fields.Float(string="Over", digits=(12, 1))
    run = fields.Selection([('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')])
    ballresult = fields.Selection([('batted', 'Batted'), ('extra', 'Extra'), ('out', 'Out')], string="Ball Result")
    selectruninextra = fields.Selection([('wide', 'Wide'), ('noball', 'Noball'), ('bye', 'Bye')], string="Select Run Extra")
    selectbatsmanisout = fields.Selection([('bowled', 'Bowled'), ('catch', 'Catch')], string="Select Batsman Out")
    stricker_id = fields.Many2one("user.detail", string="Stricker", domain="[('user_id', 'in', tosswinnername)]")
    nonstricker_id = fields.Many2one("user.detail", string="Non-Stricker", domain="[('user_id', 'in', tosswinnername)]")
    bowler_id = fields.Many2one("user.detail", string="Bowler", domain="[('user_id','not in',tosswinnername)]")
    description = fields.Text(string="Commentry")
    toss = fields.Many2one("toss.detail", string="toss")
    tosswinnername = fields.Char(string="Batting Team")
    totalrun = fields.Integer(compute="_compute_totalrun", store=True)

    def button_run_0(self):
        self.write({'run': "0"})
        return True

    def button_run_1(self):
        self.write({'run': "1"})
        return True

    def button_run_2(self):
        self.write({'run': "2"})
        return True

    def button_run_3(self):
        self.write({'run': "3"})
        return True

    def button_run_4(self):
        self.write({'run': "4"})
        return True

    def button_run_5(self):
        self.write({'run': "5"})
        return True

    def button_run_6(self):
        self.write({'run': "6"})
        return True

    def button_run_7(self):
        self.write({'run': "7"})
        return True

    def button_run_out(self):
        self.write({'ballresult': "out"})
        return True

    def button_run_wd(self):
        self.write({'selectruninextra': "wide"})
        return True

    def button_run_nb(self):
        self.write({'selectruninextra': "noball"})
        return True

    def button_run_bye(self):
        self.write({'selectruninextra': "bye"})
        return True

    @api.onchange('run', 'totalrun')
    def _compute_totalrun(self):
        total = self.env['score.board'].search([])
        score = 0
        if total:
            for t in total:
                score = score + int(t.run)
        for r in self:
            r.totalrun = score

    @api.onchange('toss')
    def onchange_getData(self):
        toss_data = self.env.context.get('current_id')
        rec = self.env['toss.detail'].browse([toss_data])
        if rec.decide == 'batting':
            self.tosswinnername = rec.tosswinnername.name
        else:
            if rec.tosswinnername.name == rec.name.team2name_id.name:
                self.tosswinnername = rec.name.team1name_id.name
            else:
                self.tosswinnername = rec.name.team2name_id.name
