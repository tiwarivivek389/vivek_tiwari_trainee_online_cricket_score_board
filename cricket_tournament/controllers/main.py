from odoo import http

class Tournament(http.Controller):
	@http.route('/tournament/', auth='public',website=True,csrf=False)
	def index(self):
		Tournament = http.request.env['tournament.detail']
		return http.request.render('cricket_tournament.index', {
			'tournaments': Tournament.search([])
		})

	@http.route(['/tournament/form','/tournament/form/<model("tournament.detail"):tournament>'],auth='public',website=True,csrf=False)
	def CreateEditForm(self, tournament=None):
		if tournament:
			tournament=http.request.env['tournament.detail'].browse([tournament.id])
		return http.request.render("cricket_tournament.tournamentform",{'tournament':tournament})

	@http.route(['/tournament/record','/tournament/record/<int:tournament>'],auth='public',website=True,method="post",csrf=False)
	def createEdit(self, tournament=None,**post):
		if post:
			if tournament:
				http.request.env['tournament.detail'].browse([tournament]).write(post)
			else:
				http.request.env['tournament.detail'].create(post)
		return http.request.redirect("/tournament")

		
	@http.route(['/tournament/delete/<model("tournament.detail"):tournament>'],auth="public",website=True,csrf=False)
	def delete(self,tournament=None):
		if tournament:
			tournament.unlink()
		return http.request.redirect('/tournament')

class ScoreBoard(http.Controller):
	@http.route('/scoreboard/',auth='public',website=True,csrf=False)
	def scoreboard(self):
		ScoreBoard = http.request.env['score.board']
		return http.request.render('cricket_tournament.scoreboard',{
			'scoreboards': ScoreBoard.search([])
			})

	@http.route(['/scoreboard/form','/scoreboard/form/<model("score.board"):scoreboard>'],auth='public',website=True,csrf=False)
	def createEditForm(self,scoreboard=None):
		if scoreboard:
			scoreboard=http.request.env['score.board'].browse([scoreboard.id])
		return http.request.render("cricket_tournament.scoreboardform",{'scoreboard':scoreboard})

	@http.route(['/scoreboard/record','/scoreboard/record/<int:scoreboard>'],auth='public',website=True,method='post',csrf=False)
	def createEdit(self,scoreboard=None,**post):
		if post:
			if scoreboard:
				http.request.env['score.board'].browse([scoreboard]).write(post)
			else:
				http.request.env['score.board'].create(post)
		return http.request.redirect("/scoreboard/")

	@http.route(['/scoreboard/delete/<model("score.board"):scoreboard>'],auth="public",website=True,csrf=False)
	def delete(self,scoreboard=None):
		if scoreboard:
			scoreboard.unlink()
		return http.request.redirect('/scoreboard/')

		




