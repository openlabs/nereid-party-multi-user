# -*- coding: utf-8 -*-
"""
    user

    :copyright: (c) 2012-2013 by Openlabs Technologies & Consulting (P) LTD
    :license: GPLv3, see LICENSE for more details.
"""
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from nereid import login_required, request, flash, redirect, url_for

__all__ = ['NereidUser', 'NereidUserParty', 'Party']
__metaclass__ = PoolMeta


class NereidUser:
    "Nereid User"
    __name__ = "nereid.user"

    party = fields.Many2One(
        'party.party', 'Party', required=True, ondelete='RESTRICT',
        select=True, depends=['parties'],
        help="Party from parties the user is currently related to"
    )
    parties = fields.Many2Many(
        'nereid.user-party.party', 'nereid_user', 'party', 'Parties',
        help="Parties to which this user is related"
    )

    @classmethod
    def create(cls, vlist):
        """
        Add the current party of the user to the list of parties allowed for
        the user automatically
        """
        users = super(NereidUser, cls).create(vlist)
        for user in users:
            if user.party not in user.parties:
                cls.write([user], {'parties': [('add', [user.party.id])]})
        return users

    @classmethod
    @login_required
    def change_party(cls, party_id):
        """
        Updates the current party of the nereid_user to the new party_id if
        it is one of the parties in the list of parties of the user

        :param party_id: ID of the party
        """
        for party in request.nereid_user.parties:
            if party.id == party_id:
                cls.write([request.nereid_user], {'party': party.id})
                break
        else:
            flash("The party is not valid")
        return redirect(
            request.args.get('next', url_for('nereid.website.home'))
        )


class NereidUserParty(ModelSQL):
    "Nereid User - Party"
    __name__ = "nereid.user-party.party"

    nereid_user = fields.Many2One(
        'nereid.user', 'Nereid User', ondelete='CASCADE',
        select=True, required=True
    )
    party = fields.Many2One(
        'party.party', 'Party', ondelete='CASCADE',
        select=True, required=True
    )


class Party:
    """
    Party
    """
    __name__ = "party.party"

    nereid_users = fields.Many2Many(
        'nereid.user-party.party', 'party', 'nereid_user', 'Nereid Users',
        help="Nereid Users which have access to this party"
    )
