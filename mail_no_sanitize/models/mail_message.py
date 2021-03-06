# -*- coding: utf-8 -*-
# Copyright 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    body = fields.Html(sanitize=False)
