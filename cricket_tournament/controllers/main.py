# -*- coding: utf-8 -*-
from odoo import http
# from odoo.http import request

class Tournament(http.Controller):
	@http.route('/tournament/', auth='public',website=True,csrf=False)
	def index(self):
		Tournament = http.request.env['tournament.detail']
		return http.request.render('cricket_tournament.index', {
			'tournaments': Tournament.sudo().search([])
		})

	@http.route(['/tournament/form','/tournament/form/<model("tournament.detail"):tournament>'],auth='public',website=True,csrf=False)
	def CreateEditForm(self, tournament=None):
		if tournament:
			tournament=http.request.env['tournament.detail'].browse([tournament.id])
		return http.request.render("cricket_tournament.tourna",{'tournament':tournament})

	@http.route(['/tournament/record','/tournament/record/<int:tournament>'],auth='public',website=True,method="post",csrf=False)
	def createEdit(self, tournament=None,**post):
		if post:
			if tournament:
				http.request.env['tournament.detail'].browse([tournament]).write(post)
			else:
				http.request.env['tournament.detail'].create(post)
		return http.request.redirect("/tournament")

		
	@http.route(['/delete/<model("tournament.detail"):tournament>'],auth="public",website=True,csrf=False)
	def delete(self,tournament=None):
		if tournament:
			tournament.unlink()
		return http.request.redirect('/tournament')





