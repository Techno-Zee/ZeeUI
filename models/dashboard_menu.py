from odoo import models, fields, api


class DashboardMenu(models.Model):
    """Class to create new dashboard menu"""
    _name = "dashboard.menu"
    _description = "Dashboard Menu"

    name = fields.Char(
        string="Name",
        required=True,
        help="Enter a name for the dashboard menu"
    )

    menu_id = fields.Many2one(
        'ir.ui.menu',
        string="Parent Menu",
        help="Parent Menu Location of New Dashboard",
        ondelete='cascade'
    )

    group_ids = fields.Many2many(
        'res.groups',
        string='Groups',
        related='menu_ref.groups_id',
        readonly=True,
        help="User must belong to one of these groups to see the menu"
    )

    client_action_id = fields.Many2one(
        'ir.actions.client',
        string="Client Action",
        readonly=True,
        ondelete='cascade'
    )

    menu_ref = fields.Many2one(
        'ir.ui.menu',
        string="Generated Menu",
        readonly=True,
        ondelete='cascade'
    )

    sequence = fields.Integer(
        string='Sequence',
        default=10
    )

    @api.model
    def create(self, vals):
        """Create new dashboard menu with action and menu"""
        # Create client action
        action = self.env['ir.actions.client'].create({
            'name': vals.get('name'),
            'tag': 'OdooDashboard',
        })
        vals['client_action_id'] = action.id

        # Create related menu
        menu = self.env['ir.ui.menu'].create({
            'name': vals.get('name'),
            'parent_id': vals.get('menu_id'),
            'action': f'ir.actions.client,{action.id}',
            'sequence': vals.get('sequence', 10),
        })
        vals['menu_ref'] = menu.id

        return super().create(vals)

    def write(self, vals):
        """Update dashboard menu, action, and related menu"""
        for rec in self:
            # Update client action name if changed
            if rec.client_action_id and 'name' in vals:
                rec.client_action_id.write({'name': vals['name']})

            # Update generated menu
            if rec.menu_ref:
                menu_vals = {}
                if 'name' in vals:
                    menu_vals['name'] = vals['name']
                if 'menu_id' in vals:
                    menu_vals['parent_id'] = vals['menu_id']
                if 'sequence' in vals:
                    menu_vals['sequence'] = vals['sequence']
                if menu_vals:
                    rec.menu_ref.write(menu_vals)

        return super().write(vals)

    def unlink(self):
        """Delete dashboard menu along with generated menu & action"""
        for rec in self:
            if rec.menu_ref:
                rec.menu_ref.unlink()
            if rec.client_action_id:
                rec.client_action_id.unlink()
        return super().unlink()
