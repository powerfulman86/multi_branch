# -*- coding: utf-8 -*-
{
    'name': "Multi Branch",
    'summary': """  Custom Application To enhance Multi Branch """,
    'description': """ Multi Branch  """,
    'author': "SIIC",
    'category': 'Other',
    'depends': ['base', 'portal', 'contacts'],
    'data': [
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/branch_views.xml',
        'views/res_users_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
