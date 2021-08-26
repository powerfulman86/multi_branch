# -*- coding: utf-8 -*-
# from odoo import http


# class MultiBranch(http.Controller):
#     @http.route('/multi_branch/multi_branch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi_branch/multi_branch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi_branch.listing', {
#             'root': '/multi_branch/multi_branch',
#             'objects': http.request.env['multi_branch.multi_branch'].search([]),
#         })

#     @http.route('/multi_branch/multi_branch/objects/<model("multi_branch.multi_branch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi_branch.object', {
#             'object': obj
#         })
