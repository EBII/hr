# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DFORMAT

class HrMedicalVisit(models.Model):
    _name = 'hr.medical.visit'
    _description = 'HR Medical Visit'

    visit_date = fields.Date(string='Visit Date')
    employee_id = fields.Many2one(comodel_name='hr.employee', required=True, string="Employee")
    visit_type = fields.Selection(selection=[
        ('HIRING', _('HIRING')),
        ('PRE REPRISE', _('PRE REPRISE')),
        ('RETURN', _('RETURN')),
        ('EMPLOYEE REQUEST', _('EMPLOYEE REQUEST')),
        ('EMPLOYER REQUEST', _('EMPLOYER REQUEST')),
        ('PERIODIQUE', _('PERIODIQUE')),
        ('DOCTOR REQUEST', _('DOCTOR REQUEST')),
        ('OTHER', _('OTHER'))
    ], string='Visit Type')
    health_center_subscription = fields.Many2one(
        comodel_name='hr.health.center.company.relation',
        string='Health center subscription', delegate=True,
        required=True)
    company_ids = fields.Many2one(related='health_center_subscription.company_ids', string="Company")
    smr_sms = fields.Selection(selection=[
        ('SMS', 'SMS'),
        ('SMR', 'SMR')
    ], string='SMS / SMR')
    visit_doctor_nurse = fields.Selection(selection=[
        ('DOCTOR', _('DOCTOR')),
        ('NURSE', _('NURSE'))
    ], string="Doctor / Nurse")
    visit_result = fields.Selection(selection=[
        ('FIT', _('FIT')),
        ('FIT WITH JOB ACCOMODATIONS', _('FIT WITH JOB ACCOMODATIONS')),
        ('UNFIT', _('UNFIT')),
        ('TEMPORARILY UNFIT - SCHUDLE VISIT', _('TEMPORARILY UNFIT - SCHEDULE VISIT')),
        ('ABSENTEE - TO RESCHEDULE', _('ABSENTEE - TO RESCHEDULE')),
        ('AWAITING THE RESULT', _('AWAITING THE RESULT')),
    ], string="Visit Result")
    visit_follow = fields.Selection(selection=[
        ('UP TO DATE', _('UP TO DATE')),
        ('TO COVENE', _('TO COVENE')),
        ('COVENING ASKED', _('COVENE ASKED')),
        ('COVENED', _('COVENED')),
        ('EXIT OF STAFF', _('EXIT OF STAFF')),
    ], string="Monitoring")
    medical_recommendation_restriction = fields.Text(string='Medical Recommendations Restriction')
    next_visit_date = fields.Date(string='Next Visit Date', readonly=True, compute='_compute_next_visit_date') # pas de champs reunion du 07 juin
    comment = fields.Text('Comment')

    @api.multi
    def _compute_next_visit_date(self):
        for res in self:
            if res.visit_date:
                visit_date = datetime.strptime(res.visit_date, OE_DFORMAT).date()
                res.next_visit_date = visit_date + relativedelta(years=5)
