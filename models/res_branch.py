# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'System Branches'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char('Branch')
    notes = fields.Text('Notes')
    active = fields.Boolean('Active', default=True, tracking=True,
                            help="Set active to false to hide the Branch without removing it.")
    user_ids = fields.Many2many(
        'res.users',
        'branch_res_users_rel',
        string='Branch Users',
        help='Users have added here, them will see any datas have linked to this Branch'
    )


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one(
        'res.branch',
        string='Branch Assigned',
        help='This is branch default for any records data create by this user'
    )
