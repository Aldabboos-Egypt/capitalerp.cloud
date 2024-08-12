# -*- coding: utf-8 -*-
import random
import string

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    number_of_users = fields.Integer(string='Number of Users')
    dabbos_reference_number = fields.Char(string='Dabbos Reference Number' )

    def generate_reference_number(self):
        prefix = "M"
        total_length = 18
        char_length = 5
        digit_length = total_length - len(prefix) - char_length

        letters = random.choices(string.ascii_letters, k=char_length)
        digits = random.choices(string.digits, k=digit_length)

        suffix = letters + digits
        random.shuffle(suffix)
        suffix = ''.join(suffix)

        self.dabbos_reference_number = prefix + suffix


    _sql_constraints = [
        ('dabbos_reference_number_unique', 'unique(dabbos_reference_number)', 'The Unique Number must be unique!')
    ]