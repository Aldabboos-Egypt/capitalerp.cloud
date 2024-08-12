# -*- coding: utf-8 -*-
# from odoo import http


# class DabbosSubscription(http.Controller):
#     @http.route('/dabbos_subscription/dabbos_subscription', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dabbos_subscription/dabbos_subscription/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dabbos_subscription.listing', {
#             'root': '/dabbos_subscription/dabbos_subscription',
#             'objects': http.request.env['dabbos_subscription.dabbos_subscription'].search([]),
#         })

#     @http.route('/dabbos_subscription/dabbos_subscription/objects/<model("dabbos_subscription.dabbos_subscription"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dabbos_subscription.object', {
#             'object': obj
#         })

