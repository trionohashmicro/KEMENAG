from odoo import models, fields, api
from datetime import datetime,date
from odoo.exceptions import UserError


class Survey(models.Model):
    _inherit = 'survey.survey'
    event_id = fields.Many2one(comodel_name="event.event", string="Event", required=False)



class EventEvent(models.Model):
    _inherit = 'event.event'
    survey_id=fields.Many2one('survey.survey')

    def create_survey(self):
        survey_create=self.env['survey.survey'].create({'title':self.name, 'event_id':self.id})
        self.survey_id=survey_create
        return {
            "type": "ir.actions.act_window",
            "res_model": "survey.survey",
            "res_id":survey_create.id,
            "views": [[False, "form"]],
            "target": "new"
        }



    def view_survey(self):
        domain = [('event_id', '=', self.id)]
        return{
            "type": "ir.actions.act_window",
            "res_model": "survey.survey",
            "views": [[False, "tree"], [False, "form"]],
            "domain":domain,
            "target": "current"
            }
