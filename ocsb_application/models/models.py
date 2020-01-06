from odoo import models, fields, api

class TournamentDetail(models.Model):
	_name="tournament.detail"
	_discription="Tournament Detail"

	name=fields.Char(string="Name",required=True)
	place=fields.Text(string="Place")
	team=fields.Integer()
	starting_date=fields.Date()
	ending_date=fields.Date()

class MatchDetail(models.Model):
	_name="match.detail"
	_discription="Match Detail"

	name=fields.Char(string="Name",required=True)
	teama_name=fields.Many2one("team.detail",string="teama_name")
	teamb_name=fields.Many2one("team.detail",string="teamb_name")
	match_type=fields.Char()
	# match_date=fields.Date()
	match_date_time=fields.Datetime()
	match_venue=fields.Text()
	umpire_name=fields.Many2many("umpire.detail",string="umpire name")

class TeamDetail(models.Model):
	_name="team.detail"
	_discription="Team Detail"

	name=fields.Char(string="Name",required=True)
	player_name=fields.Many2many("player.detail",string="player name")
	extra_player_name=fields.One2many("player.detail","player_id",string="player name")
	captain_name=fields.Many2one("player.detail",string="captain_name")
	vice_captain_name=fields.Many2one("player.detail",string="vice_captain_name")
	wicket_keepar_name=fields.Many2one("player.detail",string="wicket_keepar_name")
	# player_ids=fields.One2many("player.detail","player_id",string="player name")

class PlayerDetail(models.Model):
	_name="player.detail"
	_discription="Player Detail"

	name=fields.Char(string="Name",required=True)
	image=fields.Binary()
	address=fields.Text()
	age=fields.Integer()
	role=fields.Char()
	batting_style=fields.Char()
	bowling_style=fields.Char()
	player_id=fields.Many2one('team.detail',string="player team",ondelete="restrict")

	@api.constrains('age')
	def _check_age(self):
		for record in self:
			if record.age < 18:
				raise ValidationError("you not allow to play: %s"%record.age)
	

class UmpireDetail(models.Model):
	_name="umpire.detail"
	_discription="Umpire Detail"

	name=fields.Char(string="Name",required=True)
	image=fields.Binary()
	address=fields.Text()

class PrizeCaremony(models.Model):
	_name="prize.caremony"
	_discription="Prize Caremony"

	name=fields.Char(string="Name",required=True)
	receiver_name=fields.Char()
	giver_name=fields.Char()
	amount=fields.Integer()

# class ScoreBoard(models.Model)
# 	_name="score.board"
# 	_discription="Score Board"

class User(models.Model):
	_name="user.user"
	_discription="User User"

	name=fields.Char(string="user name",required=True)

		
