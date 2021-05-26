# -*- coding: utf-8 -*-
# from odoo import http


# class ItlSaleReferrerId(http.Controller):
#     @http.route('/itl_sale_referrer_id/itl_sale_referrer_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itl_sale_referrer_id/itl_sale_referrer_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('itl_sale_referrer_id.listing', {
#             'root': '/itl_sale_referrer_id/itl_sale_referrer_id',
#             'objects': http.request.env['itl_sale_referrer_id.itl_sale_referrer_id'].search([]),
#         })

#     @http.route('/itl_sale_referrer_id/itl_sale_referrer_id/objects/<model("itl_sale_referrer_id.itl_sale_referrer_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itl_sale_referrer_id.object', {
#             'object': obj
#         })
