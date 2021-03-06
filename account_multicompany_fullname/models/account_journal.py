# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.multi
    def name_get(self):
        res = super(AccountJournal, self).name_get()
        new_list = []
        for item in res:
            if item and item[1]:
                Journal = self.env['account.journal']
                company = Journal.browse(item[0]).company_id
                company_name = company and company.name or ''
                fullname = item[1] + ' - ' + company_name
                new_list.append((item[0], fullname))
        return new_list
