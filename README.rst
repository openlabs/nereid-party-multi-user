Nereid Party Mutli User
=======================

In B2B business application there could be multiple users on a client side
who will demand access to a web application that you might be building. In
such cases, the name of the user displayed on the portal should be of the
user and not of the party the user belongs to (default behaviour), since
the party represents the client company behing the user and not the user
himself.

This module addresses the problem by making the `display_name` field (a
function field in the core of nereid) into a `fields.Char`. This allows
a separate name for the `nereid.user` from that of the `party.party`.

Migration
=========

If your application already has users before installing the module, you
might want to migrate the name of the users from `party.party` to the 
new `display_name` field in `nereid.user`. You can use the following SQL
query for that::

    UPDATE nereid_user 
        SET display_name = party.name 
        FROM party_party AS party 
    WHERE party.id=nereid_user.party;
