# -*- coding: utf-8 -*-
# from odoo import http


# class OcsbApplication(http.Controller):
#     @http.route('/ocsb_application/ocsb_application/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ocsb_application/ocsb_application/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ocsb_application.listing', {
#             'root': '/ocsb_application/ocsb_application',
#             'objects': http.request.env['ocsb_application.ocsb_application'].search([]),
#         })

#     @http.route('/ocsb_application/ocsb_application/objects/<model("ocsb_application.ocsb_application"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ocsb_application.object', {
#             'object': obj
#         })
