# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ExpenseTemplate(models.Model):
    _name = 'expense.template'

    name = fields.Char(string="Name")
    
    expense_line_ids = fields.One2many('hr.expense', 'template_id', string='Expense Lines')


class HRExpense(models.Model):
    _inherit= 'hr.expense'

    template_id = fields.Many2one('expense.template')

class Event(models.Model):
    _inherit= 'event.event'

    @api.multi
    def action_submit_expense(self):
        self.ensure_one()
        employee = self.env['hr.employee'].search([
            ('user_id', '=', self.env.user.id)
        ], limit=1)
        
        registrations = self.mapped('registration_ids')
        attendees = registrations.mapped('partner_id')

        
        if self.expense_template_id:
            expense_line_ids = self.expense_template_id.mapped('expense_line_ids')
        
            if employee.address_id and employee.address_id.id in attendees.ids or employee.address_home_id \
                and employee.address_home_id.id in attendees.ids:
                
                expenses = []
                for expense_line in expense_line_ids:
                        data = expense_line._onchange_product_id()
                        account = expense_line.product_id.product_tmpl_id._get_product_accounts()['expense']

                        expenses.append([0, 0, {
                            'product_id': expense_line.product_id.id,
                            'name' : expense_line.name or expense_line.product_id.display_name or '',
                            'unit_amount': expense_line.product_id.price_compute('standard_price')[expense_line.product_id.id],
                            'product_uom_id' : expense_line.product_id.uom_id and expense_line.product_id.uom_id.id,
                            'tax_ids' : [(6, 0, expense_line.product_id.supplier_taxes_id.ids)],
                            'account_id':account and account.id or False

                        }])

                sheet_id = self.env['hr.expense.sheet'].create({'employee_id':employee.id, 'department_id':employee.department_id.id,
                                 'event_id':self.id, 'name':self.name + ' - ' + employee.name,
                                 'expense_line_ids':expenses})
                return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form,tree',
                'res_model': 'hr.expense.sheet',
                'target': 'current',
                'context': {},
                'res_id': sheet_id.id,
                'domain': [('id', '=', sheet_id.id)],
                
            } 

            else:
                raise UserError(_("Expenses can only submitted by registered employee for this event."))
        else:
                raise UserError(_("Expense Template is not set."))

        return True

    expense_template_id = fields.Many2one('expense.template')

class hr_expense_sheet(models.Model):
    _inherit = 'hr.expense.sheet'
    
    event_id = fields.Many2one('event.event')
