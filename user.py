# -*- coding: utf-8 -*-
"""
    user

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) LTD
    :license: GPLv3, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields


class NereidUser(ModelSQL, ModelView):
    "Nereid User"
    _name = "nereid.user"

    display_name = fields.Char('Display Name', required=True, select=True)

NereidUser()
