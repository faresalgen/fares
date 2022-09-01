# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"


    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True, copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    active = fields.Boolean(string="Active", default=True)
