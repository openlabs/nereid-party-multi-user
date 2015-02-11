Nereid Party Multi User
=======================

[![Build Status](https://travis-ci.org/openlabs/nereid-party-multi-user.svg?branch=develop)](https://travis-ci.org/openlabs/nereid-party-multi-user)
[![Downloads](https://pypip.in/download/trytond_nereid-party-multi-user/badge.svg)](https://pypi.python.org/pypi/trytond_nereid-party-multi-user/)
[![Latest Version](https://pypip.in/version/trytond_nereid-party-multi-user/badge.svg)](https://pypi.python.org/pypi/trytond_nereid-party-multi-user/)
[![Development Status](https://pypip.in/status/trytond_nereid-party-multi-user/badge.svg)](https://pypi.python.org/pypi/trytond_nereid-party-multi-user/)
[![Coverage Status](https://coveralls.io/repos/openlabs/nereid-party-multi-user/badge.svg?branch=develop)](https://coveralls.io/r/openlabs/nereid-party-multi-user?branch=develop)

Introduction
------------

This module addresses the following issues:

1. A nereid user having multiple parties associated to it.

    Useful in cases where a single user may need access to multiple
    parties. For example if both supplier A and supplier B have the same
    accountant who needs access to the portal, the parties could be added
    to the nereid user and the user could switch between the two
    companies.

    Tip: Nereid design mostly uses the current party identified by the
    `party` field in nereid for filtering and displaying relevant
    information to a customer. So switching of the party would be
    necessary for user's information context to change.

2. A party having multiple users associated to it.

    In B2B applications it is often the case that there are multiple users
    for the same party. For example, if you have built a portal, you might
    want to grant access to the owner as well as the accountant. In this
    case two nereid users could be related to the same party.

3. Having a name separate from the party.

    In B2B business application there could be multiple users on a client side
    who will demand access to a web application that you might be building. In
    such cases, the name of the user displayed on the portal should be of the
    user and not of the party the user belongs to (default behaviour), since
    the party represents the client company behind the user and not the user
    himself.

This module addresses the problem by making the `display_name` field (a
function field in the core of nereid) into a `fields.Char`. This allows
a separate name for the `nereid.user` from that of the `party.party`.

Migration
=========

If your application already has users before installing the module, you
might want to follow the migration path explained below:


To migrate the existing m2o/o2m relationship between party and nereid user
--------------------------------------------------------------------------

SQL:

    INSERT INTO "nereid_user-party_party" (nereid_user, party) (
        SELECT  id AS nereid_user, party FROM nereid_user
    );

To migrate the name of the `party` as the `display_name`
--------------------------------------------------------

SQL:

    UPDATE nereid_user
        SET display_name = party.name
        FROM party_party AS party
    WHERE party.id=nereid_user.party;
