# -*- coding: utf-8 -*-
"""
    __init__

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) LTD
    :license: GPLv3, see LICENSE for more details.
"""
from trytond.pool import Pool
from .user import NereidUser, NereidUserParty, Party


def register():
    Pool.register(
        NereidUser,
        NereidUserParty,
        Party,
        module='nereid_party_multi_user', type_='model')
