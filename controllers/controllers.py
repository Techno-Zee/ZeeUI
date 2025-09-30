# -*- coding: utf-8 -*-
# from odoo import http


# class ZeeUi(http.Controller):
#     @http.route('/zee_ui/zee_ui', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zee_ui/zee_ui/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zee_ui.listing', {
#             'root': '/zee_ui/zee_ui',
#             'objects': http.request.env['zee_ui.zee_ui'].search([]),
#         })

#     @http.route('/zee_ui/zee_ui/objects/<model("zee_ui.zee_ui"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zee_ui.object', {
#             'object': obj
#         })

