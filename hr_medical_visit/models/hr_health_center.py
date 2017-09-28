# -*- coding: utf-8 -*-
from odoo import fields, models, api

class HrHealthCenter(models.Model):
    _name = 'hr.health.center'
    _description = 'HR Health Center'

    name = fields.Char(string='Name')
    display_name = fields.Char(compute='_display_name')
    address_id = fields.Many2one(comodel_name='res.partner', string='Address')
    company_relation_ids = fields.One2many(comodel_name='hr.health.center.company.relation',
                                                inverse_name='health_center_id', string="Company Relation")
    comment = fields.Text(string='Comment')

class HrHealthCenterRelation(models.Model):
    _name = 'hr.health.center.company.relation'
    _description = 'HR Health Center Company Relation'

    name = fields.Char(string='Subscription Number')
    health_center_id = fields.Many2one(comodel_name='hr.health.center', required=True, string='Health Center')
    company_ids = fields.Many2one('res.company', required=True, string='Company')
    subscription_date = fields.Date(string='Subscription date')
    complements = fields.Text(string='Additional information')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Subscription Number already exists!')
    ]

    @api.multi
    @api.depends('name')
    def _display_name(self):
        for rec in self:
                if rec.address_id.city:
                    rec.display_name = rec.name + " - " + rec.address_id.city
                else:
                    rec.display_name = rec.name