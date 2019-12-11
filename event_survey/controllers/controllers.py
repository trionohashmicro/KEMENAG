# -*- coding: utf-8 -*-
from odoo import http

# class EventSurvey(http.Controller):
#     @http.route('/event_survey/event_survey/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_survey/event_survey/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_survey.listing', {
#             'root': '/event_survey/event_survey',
#             'objects': http.request.env['event_survey.event_survey'].search([]),
#         })

#     @http.route('/event_survey/event_survey/objects/<model("event_survey.event_survey"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_survey.object', {
#             'object': obj
#         })