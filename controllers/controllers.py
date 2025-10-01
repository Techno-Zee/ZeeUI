# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ZeeUi(http.Controller):
    """Class to search and filter values in dashboard"""

    @http.route('/api/zee_ui/dashboard_search', type='json', auth='user')
    def dashboard_search(self, search_input):
        """Filter dashboard blocks by name"""
        blocks = request.env['dashboard.block'].sudo().search([
            ('name', 'ilike', search_input)
        ])
        return blocks.ids

    @http.route('/api/zee_ui/check_access', type='json', auth='user')
    def check_access(self):
        """Check access rights of the current user in custom dashboard groups"""
        user = request.env.user
        return {
            "is_user": user.has_group("zee_ui.group_dashboard_user"),
            "is_manager": user.has_group("zee_ui.group_dashboard_manager"),
            "is_admin": user.has_group("zee_ui.group_dashboard_admin"),
        }
