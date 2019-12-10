# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class EventRegistration(models.Model):
    _inherit = "event.registration"

    att_image = fields.Binary(string="Image")
    full_name = fields.Char(string="Full Name")
    nip = fields.Char(string="NIP")
    rank_catagory = fields.Char(string="Rank/Category")
    position = fields.Char(string="Position")
    working_unit = fields.Char(string="Working Unit")
    place_dob = fields.Char(string="Place & Date of Birth")
    address = fields.Char(string="Address")
    ofc_address = fields.Char(string="Office Address")
    ofc_phone = fields.Char(string="Office Phone")
    cellphone = fields.Char(string="Cellphone")
    bg_education = fields.Text(string="Background Education")
    w_p_expr = fields.Text(string="Working/Position Experience")
    npwp = fields.Char(string="NPWP")
    bank_name = fields.Char(string="Bank Name")
    acc_number = fields.Char(string="Account Number")
    latter_of_duty = fields.Binary(string="Letter of Duty")
    file_name = fields.Char(string="File name")
