# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class Home(Home):
    def _login_redirect(self, uid, redirect=None):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('cricket_tournament.group_organizer'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_portal'):
            return '/yourhomepage'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return '/web/'
        return super(Register, self)._login_redirect(uid, redirect=redirect)


class Register(http.Controller):
    @http.route('/userregister/', auth="public", type="http", csrf=False)
    def customer_register(self, **kw):
        currency = request.env['res.currency'].sudo().search([])
        return request.render('cricket_tournament.organizer', {'currency': currency})

    @http.route('/userregister/form', auth="public", method="post", type="http", csrf=False)
    def register(self, **post):
        if post.get('login') == 'serviceprovider':
            group_id_name = [(6, 0, [request.env.ref('cricket_tournament.group_organizer').id, http.request.env.ref('base.group_user').id])]
            currency_name = post.get('currency')
            currency = request.env['res.currency'].sudo().search([('name', '=', currency_name)], limit=1)
            partner = request.env['res.partner'].sudo().create({
                'name': post.get('username'),
                'email': post.get('email')
                })
            company = request.env['res.company'].sudo().create({
                'name': post.get('companyname'),
                'partner_id': partner.id,
                'currency_id': currency.id,
                })
            request.env['res.users'].sudo().create({
                'partner_id': partner.id,
                'login': post.get('username'),
                'password': post.get('password'),
                'company_id': company.id,
                'company_ids': [(4, company.id)],
                'groups_id': group_id_name,
                })
        else:
            group_id_name = [(6, 0, [request.env.ref('base.group_portal').id])]
            partner = request.env['res.partner'].sudo().create({
                'name': post.get('username'),
                'email': post.get('email')
                })
            request.env['res.users'].sudo().create({
                'partner_id': partner.id,
                'login': post.get('username'),
                'password': post.get('password'),
                'groups_id': group_id_name,
                })
        return http.local_redirect('/web/login')


class User_Portal(http.Controller):
    @http.route('/yourhomepage/', auth='public', type="http", csrf=False)
    def index(self, **kw):
        Tournament = request.env['tournament.detail'].sudo().search([])
        return request.render('cricket_tournament.sub', {
            'tournaments': Tournament.search([])
            })

    @http.route('/summary/', auth='public', type="http", csrf=False)
    def summary(self, **kw):
        Tournament = request.env['tournament.detail'].sudo().search([])
        return request.render('cricket_tournament.match_form', {
            'tournaments': Tournament.search([])
            })

    @http.route('/match_detail/', auth='public', type="http", csrf=False)
    def MatchDetail(self, **kw):
        Match = request.env['match.detail'].sudo().search([])
        return request.render('cricket_tournament.match', {
            'matchs': Match.search([])
            })

    @http.route(['/tournament_shedule/<string:m_id>'], auth='public', type='http', csrf=False)
    def shedule(self, m_id=None, **kw):
        if m_id:
            Match = request.env['tournament.detail'].sudo().browse([m_id])
            Shedule = request.env['match.detail'].sudo().search([('match_id', '=', int(Match.id))])
        return request.render('cricket_tournament.match', {
            'matchs': Shedule
            })

    @http.route('/form/', auth='public', type='http', csrf=False)
    def form(self, **kw):
        return request.render('cricket_tournament.match_form')

    @http.route('/team_detail/', auth='public', type='http', csrf=False)
    def TeamDetail(self, **kw):
        Team = request.env['team.detail'].sudo().search([])
        return request.render('cricket_tournament.match_form', {
            'teams': Team.search([])
            })
