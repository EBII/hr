# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class HrCollectiveagreement(models.Model):
    _name = 'hr.collective.agreement'
    _description = 'HR Collective Agreement'


    name = fields.Char("Name", required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
