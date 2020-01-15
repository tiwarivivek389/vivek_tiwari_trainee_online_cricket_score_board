from odoo import models,api,fields

class TournamentDetail(models.Model):
	_name="tournament.detail"
	_discription="Tournament Detail"

	name=fields.Char(string="Tournament name",required=True)
	place=fields.Char(string="Tournament Place")
	team=fields.Integer(string="Participate Team")
	starting_date=fields.Date(string="Tournament Starting Date")
	ending_date=fields.Date(string="Tournament Ending Date")

	# @api.model
	# def create(self, values):
	# 	record=super(TournamentDetail, self).create(values)
	# 	return record

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


