# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class exe_pos_srkiosquero(models.Model):
#     _name = 'exe_pos_srkiosquero.exe_pos_srkiosquero'
#     _description = 'exe_pos_srkiosquero.exe_pos_srkiosquero'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
