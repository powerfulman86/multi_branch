# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
import logging

_logger = logging.getLogger(__name__)


class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'System Branches'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char('Branch', translate=True, required=True)
    internal_reference = fields.Char(string="Internal Reference", required=True, size=2)
    notes = fields.Text('Notes')
    active = fields.Boolean('Active', default=True, tracking=True,
                            help="Set active to false to hide the Branch without removing it.")
    user_ids = fields.Many2many(
        'res.users',
        'branch_res_users_rel',
        string='Branch Users',
        help='Users have added here, them will see any datas have linked to this Branch'
    )

    sale_sequence_id = fields.Many2one('ir.sequence', 'Sale Sequence', copy=False, readonly=True)

    _sql_constraints = [
        (
            "branch_code_uniq",
            "unique(internal_reference)",
            "Branch Code must be unique across the database!",
        )
    ]

    @api.model
    def create(self, vals):
        vals['sale_sequence_id'] = self.env['ir.sequence'].create({
            'name': _('Sale_Sequence_') + vals['name'],
            'prefix': 'S%(y)s' + vals['internal_reference'], 'padding': 4,
            'company_id': self.env.company.id, }).id

        return super(ResBranch, self).create(vals)

    def write(self, vals):
        if not self.sale_sequence_id:
            vals['sale_sequence_id'] = self.env['ir.sequence'].create({
                'name': _('Sale_Sequence_') + self.name,
                'prefix': 'S%(y)s' + self.internal_reference, 'padding': 4,
                'company_id': self.env.company.id, }).id
        return super(ResBranch, self).write(vals)

    @api.constrains('internal_reference')
    def constrains_internal_reference(self):
        for rec in self:
            if not rec.internal_reference.isdigit():
                raise ValidationError(_("Branch Number Must Be In Digits"))

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

    def get_default_branch(self):
        return self.env['res.branch'].search([], limit=1, order='id').id


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one(
        'res.branch',
        string='Branch Assigned',
        help='This is branch default for any records data create by this user'
    )
