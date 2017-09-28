# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class HrEmploymentGroupLevel(models.Model):
    _name = 'hr.employment.group.level'
    _description = 'HR Employment Group Level'

    name = fields.Char(string='NIVEAU/GROUPE', required=True)
    collective_agreement_id = fields.Many2one(comodel_name='hr.collective.agreement', string='Collective Agreement', required=True)

    _sql_constraints = [('unique_key_per_group_level',
                         'unique(name, collective_agreement_id)',
                         'Uniqueness Constraint : Already exists in database')]
    @api.multi
    @api.depends('name', 'collective_agreement_id')
    def _get_display_name(self):
        for res in self:
            if res.name:
                if res.collective_agreement_id.name:
                    texte = [res.name, res.collective_agreement_id.name]
                    res.display_name = ": ".join(texte)

class HrEmploymentGroupCoef(models.Model):
    _name = 'hr.employment.group.coef'
    _description = 'HR Employment Group Coef'

    name = fields.Integer(string='COEF/SEUIL', required=True)
    collective_agreement_id = fields.Many2one(comodel_name='hr.collective.agreement', string='Collective Agreement', required=True)

    _sql_constraints = [('unique_key_per_group_level',
                         'unique(name, collective_agreement_id)',
                         'Uniqueness Constraint : Already exists in database')]

    # @api.multi
    # @api.depends('name', 'collective_agreement_id')
    # def _get_display_name(self):
    #     for res in self:
    #         if res.name:
    #             if res.collective_agreement_id.name:
    #                 texte = [str(res.name), res.collective_agreement_id.name]
    #                 res.display_name = ": ".join(texte)
