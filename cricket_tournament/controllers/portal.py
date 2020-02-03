from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class Home(Home):
	def _login_redirect(self, uid, redirect=None):
		if http.request.session.uid and http.request.env['res.users'].sudo().browse(http.request.session.uid).has_group('cricket_tournament.group_organizer'):
			return '/web/'
		if http.request.session.uid and http.request.env['res.users'].sudo().browse(http.request.session.uid).has_group('base.group_portal'): 
			return '/yourhomepage'
		if http.request.session.uid and http.request.env['res.users'].sudo().browse(http.request.session.uid).has_group('base.group_user'): 
			return '/web/'
		return super(Register, self)._login_redirect(uid, redirect=redirect)



class Register(http.Controller):
	@http.route('/userregister/',auth="public",type="http",csrf=False)
	def customer_register(self,**kw):
		currency = http.request.env['res.currency'].sudo().search([])
		return http.request.render('cricket_tournament.organizer',{'currency':currency})


	@http.route('/yourhomepage',auth='public',type="http",csrf=False)
	def index(self,**kw):
		Tournament = http.request.env['tournament.detail'].sudo().search([])
		return http.request.render('cricket_tournament.sub',{
			'tournaments':Tournament.search([])
			})

	@http.route(['/tournament_shedule/<model(match.detail):match>'],auth='public',type='http',csrf=False)
	def shedule(self, match=None):
		Match = request.env['match.detail'].sudo().search([match.id])
		return request.render('cricket_tournament.match',{
			'matchs':Match
			})


	@http.route('/userregister/form',auth="public",method="post",type="http",csrf=False)
	def register(self,**post):
		if post.get('login') == 'serviceprovider':
			group_id_name=[(6,0,[http.request.env.ref('cricket_tournament.group_organizer').id])]
			currency_name=post.get('currency')
			currency=http.request.env['res.currency'].sudo().search([('name','=',currency_name)],limit=1)
			partner=http.request.env['res.partner'].sudo().create({
				'name':post.get('username'),
				'email':post.get('email')
				})
			company=http.request.env['res.company'].sudo().create({
				'name':post.get('companyname'),
				'partner_id':partner.id,
				'currency_id':currency.id,
				})
			http.request.env['res.users'].sudo().create({
				'partner_id':partner.id,
				'login':post.get('username'),
				'password':post.get('password'),
				'company_id':company.id,
				'company_ids':[(4,company.id)],
				'groups_id':group_id_name,
				})
		else:
			group_id_name=[(6,0,[http.request.env.ref('base.group_portal').id])]
			partner=http.request.env['res.partner'].sudo().create({
				'name':post.get('username'),
				'email':post.get('email')
				})
			http.request.env['res.users'].sudo().create({
				'partner_id':partner.id,
				'login':post.get('username'),
				'password':post.get('password'),
				'groups_id':group_id_name,
				})
		return http.local_redirect('/web/login')		


