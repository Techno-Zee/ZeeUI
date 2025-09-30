# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class zee_ui(models.Model):
#     _name = 'zee_ui.zee_ui'
#     _description = 'zee_ui.zee_ui'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

