# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class EventProject(models.Model):
    _inherit = "event.event"

    project_id = fields.Many2one('project.project', string="Project")
