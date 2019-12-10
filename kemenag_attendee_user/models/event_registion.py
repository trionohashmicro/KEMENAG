# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class EventRegistration(models.Model):
    _inherit = "event.registration"

 

    @api.one
    def confirm_registration(self):
        self.state = 'open'
        user = self.env['res.users'].create({
    	      'name': self.name,
              'login': self.email})
        # auto-trigger after_sub (on subscribe) mail schedulers, if needed
        onsubscribe_schedulers = self.event_id.event_mail_ids.filtered(
            lambda s: s.interval_type == 'after_sub')
        onsubscribe_schedulers.execute()
        return user
