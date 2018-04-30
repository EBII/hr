# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DFORMAT
from datetime import datetime

# class HrDpoDesk(models.Model):
#     _name = 'hr.dpo.desk'
#     _description = 'HR Data Protector Desk'
#

class DpoRequest(models.Model):
    _name = 'hr.dpo.request'
    _description = 'Follow Personnal Data Request'

    name = fields.Char(string="intitulé de la demande")
    content = fields.Text(string="Description de la demande")
    comment = fields.Text(string="Commentaire sur demande")
    action_ids = fields.Many2many(comodel_name='hr.dpo.action',
                                        relation='dpo_request_action_rel',
                                        column1='request_id',
                                        column2='action_id',
                                        string='Action')

    service = fields.Char(string="Service concerné")
    employee = fields.Many2one(comodel_name="hr.employee", string="responsable")
    state = fields.Selection([
        ('receive', _('Receive')),
        ('running', _('Running')),
        ('close', 'Release'),
    ], string='Status', track_visibility='onchange',
        help='Status of the request', default='receive')

class DpoAction(models.Model):
    _name = 'hr.dpo.action'
    _description = 'Action to answers request'

    name = fields.Char(string="Intitulé de l'action")
    description = fields.Text(string="Description de l'action")
    comment = fields.Text(string="Commentaire sur demande")
    request_id = fields.Many2many(comodel_name='hr.dpo.request',
                                        relation='dpo_request_action_rel',
                                        string='Demande')
    treatment_id = fields.Many2many(comodel_name='hr.dpo.request',
                                        relation='dpo_request_action_rel',
                                        string='Demande')

    period = fields.Selection([
        ('Single', _('Single')),
        ('Mensuelle', _('Mensuelle')),
        ('Trimestrielle', _('Trimestrielle')),
        ('Annuelle', _('Annuelle')),
    ], string="Periodicity", default='Single')
    state = fields.Selection([
        ('todo', _('Todo')),
        ('close', _('Release')),
    ], string='Status', track_visibility='onchange',
        help='Status of the action', default='todo')

class DpoTreatment(models.Model):
    _name ='hr.dpo.treatment'
    _description = 'Periodic action'

    name = fields.Char(string="intitulé de l'operation")
    action_ids = fields.Many2many(comodel_name='hr.dpo.action',
                                  relation='dpo_treatment_action_rel',
                                  column1='treatment_id',
                                  column2='action_id',
                                  string='Action')
    state = fields.Selection([
        ('todo', _('Todo')),
        ('running', _('Running')),
        ('close', 'Release'),
    ], string='Status', track_visibility='onchange',
        help='Status of the request', default='running')

class DpoDocument(models.Model):
    _name = "hr.dpo.document"
    _description = "RGPD Documents manage by Dpo"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    attachment_ids = fields.One2many(
        comodel_name='ir.attachment', inverse_name='res_id', domain=lambda self: [
            ('res_model', '=', self._name)], string='Attachments')
    type = fields.Selection([
        ('TEMPLATE', _('TEMPLATE')),
        ('SIGNED', _('SIGNED'))
    ], string='Type')

