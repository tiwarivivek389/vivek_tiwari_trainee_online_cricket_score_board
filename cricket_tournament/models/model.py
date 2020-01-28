from odoo import models,api,fields
from odoo import http

class TournamentDetail(models.Model):
	_name="tournament.detail"
	_description="Tournament Detail"

	name=fields.Char(string="Tournament name",required=True)
	place=fields.Char(string="Tournament Place")
	tournamenttype=fields.Selection([
		('latherballtournament','Leather Ball Tournaments'),
		('tennisballtournament','Tennis Ball Tournaments'),
		('underarmstournament','Underarms Tournaments'),
		('tapeballtournament','Tape Ball Tournaments')
		])
	team=fields.Integer(string="Participate Team")
	starting_date=fields.Date(string="Tournament Starting Date")
	ending_date=fields.Date(string="Tournament Ending Date")
	shedule=fields.One2many("match.detail","match_id",string="Shedule")

	@api.constrains('starting_date','ending_date')
	def check_date(self):
		for rec in self:
			if rec.ending_date < rec.starting_date:
				raise ValidationError(_('value must be greater than'))

class MatchDetail(models.Model):
	_name="match.detail"
	_description="Match Detail"

	name=fields.Char(string="Match Name",required=True)
	team1name=fields.Many2one("team.detail",string="Team1Name")
	team2name=fields.Many2one("team.detail",string="Team2Name")
	matchover=fields.Char(string="Match Over")
	matchdatetime=fields.Datetime(string="Match_Date_Time")
	umpirename=fields.Char(string="Umpire Name")
	matchvenue=fields.Text(string="Match Venue")
	color=fields.Integer()
	match_id=fields.Many2one("tournament.detail",string="match",ondelete="restrict")


class TeamDetail(models.Model):
	_name="team.detail"
	_description="Team Detail"

	name=fields.Char(string="Team Name",required=True)
	playername=fields.Many2many("user.detail",string="Player Name")
	extraplayername=fields.One2many("user.detail","user_id",string="Extra Player Name")
	captainname=fields.Many2one("user.detail",string="Captain Name")
	vicecaptainname=fields.Many2one("user.detail",string="Vice Captain Name")
	wicketkeeparname=fields.Many2one("user.detail",string="Wicket Keepar Name")

class UserDetail(models.Model):
	_name="user.detail"
	_description="User Detail"

	name=fields.Char(string="Name",required=True)
	image=fields.Binary()
	address=fields.Text()
	age=fields.Integer()
	role=fields.Selection([
		('batsman','Batsman'),
		('bowler','Bowler'),
		('allrounder','Allrounder'),
		('keeparbatsman','Keeparbatsman')
		])
	batting_style=fields.Char()
	bowling_style=fields.Char()
	user_id=fields.Many2one('team.detail',string="user",ondelete="restrict")

	@api.constrains('age')
	def _check_age(self):
		for record in self:
			if record.age < 18:
				raise ValidationError("you not allow to play: %s"%record.age)

class PrizeCaremony(models.Model):
	_name="prize.caremony"
	_description="Prize Caremony"

	name=fields.Char(string="Name",required=True)
	receiver_name=fields.Many2one("user.detail",string="Receiver Name")
	giver_name=fields.Char()
	amount=fields.Integer()
	state=fields.Selection([('confirm','Confirm'),('draft','Draft'),('done','Done')],default="confirm")

	def button_confirm(self):
		self.write({'state':"confirm"})
		return True

	def button_draft(self):
		self.write({'state':'draft'})
		return True

	def button_done(self):
		self.write({'state':'done'})
		return True

class TossDetail(models.Model):
	_name="toss.detail"
	_description="Toss Detail"

	name=fields.Many2one('match.detail',string="match name")
	team=fields.Many2many(comodel_name="team.detail",compute="_compute_team",string="Team",stored=False)
	tosswinnername=fields.Many2one('team.detail',string="Toss Winner Team", domain="[('id','in', team)]")
	decide=fields.Selection([
		('batting','Batting'),
		('bowling','Bowling')
		])
	description=fields.Text()

	@api.depends('name')
	def _compute_team(self):
		match=self.env['match.detail'].search([('id','=',self.name.id)])
		l=[match.team1name.id,match.team2name.id]
		# print(match.team1name.id,"-------------",match.team2name.id)
		self.team=self.env['team.detail'].search([('id','in',l)])	


class ScoreBoard(models.Model):
	_name="score.board"
	_description="Score Board"	

	name=fields.Selection([('firstinning','First Inning'),('secondinning','Second Inning')])
	over=fields.Integer(string="Over")
	ball=fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
	run=fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7')])	
	typeofrun=fields.Selection([
		('batted','Batted'),
		('extra','Extra'),
		('extrabatted','Extra Batted'),
		('out','Out'),
		('outbatted','Out Batted'),
		('outbattedextra','Out Batted Extra'),
		('outextra','Out Extra')
		])
	selectruninextra=fields.Selection([
		('wide','Wide'),
		('widebye','Wide Bye'),
		('noball','Noball'),
		('noballbye','Noball Bye')
		])
	selectbatsmanisout=fields.Selection([
		('bowled','Bowled'),
		('catch','Catch'),
		('lbw','LBW'),
		('stumped','Stumped'),
		('hitwicket','Hit-Wicket'),
		('runoutstricker','Runout-Stricker'),
		('runoutnonstricker','Runout-nonStricker'),
		('retirehurtstricker','Retirehurt-Stricker'),
		('retirehurtnonstricker','Retirehurt-nonStricker'),
		])
	stricker=fields.Many2one("user.detail",string="Stricker")
	nonstricker=fields.Many2one("user.detail",string="Non-Stricker")
	bowler=fields.Many2one("user.detail",string="Bowler")	

	










