# -*- coding: utf-8 -*-
# from odoo import http


# class ECommerce(http.Controller):
#     @http.route('/e_commerce/e_commerce', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e_commerce/e_commerce/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('e_commerce.listing', {
#             'root': '/e_commerce/e_commerce',
#             'objects': http.request.env['e_commerce.e_commerce'].search([]),
#         })

#     @http.route('/e_commerce/e_commerce/objects/<model("e_commerce.e_commerce"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e_commerce.object', {
#             'object': obj
#         })

