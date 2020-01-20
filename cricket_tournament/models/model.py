from odoo import models,api,fields

class TournamentDetail(models.Model):
	_name="tournament.detail"
	_discription="Tournament Detail"

	name=fields.Char(string="Tournament name",required=True)
	place=fields.Char(string="Tournament Place")
	team=fields.Integer(string="Participate Team")
	starting_date=fields.Date(string="Tournament Starting Date")
	ending_date=fields.Date(string="Tournament Ending Date")

	@api.constrains('starting_date','ending_date')
	def check_date(self):
		for rec in self:
			if rec.ending_date < rec.starting_date:
				raise ValidationError(_('value must be greater than'))

class MatchDetail(models.Model):
	_name="match.detail"
	_discription="Match Detail"

	name=fields.Char(string="Match Name",required=True)
	team1name=fields.Many2one("team.detail",string="Team1Name")
	team2name=fields.Many2one("team.detail",string="Team2Name")
	matchtype=fields.Char(string="Match Type")
	matchdatetime=fields.Datetime(string="Match_Date_Time")
	umpirename=fields.Char(string="Umpire Name")
	matchvenue=fields.Text(string="Match Venue")
	color=fields.Integer()

class TeamDetail(models.Model):
	_name="team.detail"
	_discription="Team Detail"

	name=fields.Char(string="Team Name",required=True)
	playername=fields.Many2many("user.detail",string="Player Name")
	extraplayername=fields.One2many("user.detail","user_id",string="Extra Player Name")
	captainname=fields.Many2one("user.detail",string="Captain Name")
	vicecaptainname=fields.Many2one("user.detail",string="Vice Captain Name")
	wicketkeeparname=fields.Many2one("user.detail",string="Wicket Keepar Name")

class UserDetail(models.Model):
	_name="user.detail"
	_discription="User Detail"

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
	_discription="Prize Caremony"

	name=fields.Char(string="Name",required=True)
	receiver_name=fields.Char()
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

class ScoreBoard(models.Model):
	_name="score.board"
	_discription="Score Board"

	inning=fields.Selection([('firstinning','First Inning'),('secondinning','Second Inning')])
	over=fields.Integer(string="Over")
	ball=fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
	run=fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
	stricker=fields.Many2one("user.detail",string="Stricker")
	nonstricker=fields.Many2one("user.detail",string="Non-Stricker")
	bowler=fields.Many2one("user.detail",string="Bowler")	
	typeofrun=fields.Selection([
		('batted','Batted'),
		('extra','Extra'),
		('extra,batted','Extra,Batted'),
		('out','Out'),
		('out,batted','Out,Batted')
		])
	selectruninextra=fields.Selection([
		('wide','Wide'),
		('noball','Noball'),
		('bye','Bye')
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







