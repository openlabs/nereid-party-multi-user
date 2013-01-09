# -*- coding: utf-8 -*-
"""
    user

    :copyright: (c) 2012-2013 by Openlabs Technologies & Consulting (P) LTD
    :license: GPLv3, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields
from nereid import login_required, request, flash, redirect, url_for


class NereidUser(ModelSQL, ModelView):
    "Nereid User"
    _name = "nereid.user"

    display_name = fields.Char('Display Name', required=True, select=True)
    party = fields.Many2One(
        'party.party', 'Party', required=True, ondelete='RESTRICT',
        select=True, depends=['parties'],
        help="Party from parties the user is currently related to"
    )
    parties = fields.Many2Many(
        'nereid.user-party.party', 'nereid_user', 'party', 'Parties',
        help="Parties to which this user is related"
    )

    def create(self, values):
        """
        Add the current party of the user to the list of parties allowed for
        the user automatically
        """
        user_id = super(NereidUser, self).create(values)
        if 'parties' not in values:
            user = self.browse(user_id)
            self.write(user_id, {'parties': [('add', [user.party.id])]})
        return user_id

    @login_required
    def change_party(self, party_id):
        """
        Updates the current party of the nereid_user to the new party_id if
        it is one of the parties in the list of parties of the user

        :param party_id: ID of the party
        """
        for party in request.nereid_user.parties:
            if party.id == party_id:
                self.write(request.nereid_user.id, {'party': party.id})
        else:
            flash("The party is not valid")
        return redirect(
            request.args.get('next', url_for('nereid.website.home'))
        )

NereidUser()


class NereidUserParty(ModelSQL):
    "Nereid User - Party"
    _name = "nereid.user-party.party"
    _description = __doc__

    nereid_user = fields.Many2One(
        'nereid.user', 'Nereid User', ondelete='CASCADE',
        select=True, required=True
    )
    party = fields.Many2One(
        'party.party', 'Party', ondelete='CASCADE',
        select=True, required=True
    )

NereidUserParty()


class Party(ModelSQL, ModelView):
    """
    Party
    """
    _name = "party.party"

    nereid_users = fields.Many2Many(
        'nereid.user-party.party', 'party', 'nereid_user', 'Nereid Users',
        help="Nereid Users which have access to this party"
    )

Party()
