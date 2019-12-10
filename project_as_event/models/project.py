# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectEvent(models.Model):
    _inherit = "project.project"

    is_event = fields.Boolean(string="Is Events")
