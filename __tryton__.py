# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{
    'name': 'Nereid Party Multi User',
    'version': '2.4.0.2dev',
    'author': 'Openlabs Technologies & Consulting (P) Ltd.',
    'email': 'info@openlabs.co.in',
    'website': 'http://www.openlabs.co.in/',
    'description': '''

Features:

  * Allow multiple users per party
  * Allow multiple parties per user
  * The module replaces the display_name field (function field)
    in nereid to a char field.

Example usage:

  * A partner portal where multiple users from your customer company will
    need access to the same party data.
  * A situation where a user may be part of multiple companies, like a
    signle bookkeeper for two of your customers

    ''',
    'depends': [
        'nereid',
    ],
    'xml': [
       'user.xml',
       'urls.xml',
    ],
    'translation': [
    ],
}
