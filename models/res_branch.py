# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'System Branches'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char('Branch', translate=True, )
    internal_reference = fields.Char(string="Internal Reference", required=False, )
    notes = fields.Text('Notes')
    active = fields.Boolean('Active', default=True, tracking=True,
                            help="Set active to false to hide the Branch without removing it.")
    user_ids = fields.Many2many(
        'res.users',
        'branch_res_users_rel',
        string='Branch Users',
        help='Users have added here, them will see any datas have linked to this Branch'
    )

    _sql_constraints = [
        (
            "branch_code_uniq",
            "unique(internal_reference)",
            "Branch Code must be unique across the database!",
        )
    ]

    def name_get(self):
        result = []
        for rec in self:
            name = ('[%s] %s' % (rec.internal_reference, rec.name))
            result.append((rec.id, name))
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        super(ResBranch, self).name_search(name)
        # args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('internal_reference', operator, name)]
        recs = self.search(domain, limit=limit)
        return recs.name_get()


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one(
        'res.branch',
        string='Branch Assigned',
        help='This is branch default for any records data create by this user'
    )
