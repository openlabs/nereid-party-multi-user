# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{
    'name': 'Nereid Party Multi User',
    'version': '2.4.0.1dev',
    'author': 'Openlabs Technologies & Consulting (P) Ltd.',
    'email': 'info@openlabs.co.in',
    'website': 'http://www.openlabs.co.in/',
    'description': '''
Module to allow multiple users per party. The module replaces the display_name
field (function field) in nereid to a char field.

Example usage:

  * A partner portal where different users from your customer company will
    need access to the same party data.
    ''',
    'depends': [
        'nereid',
    ],
    'xml': [
       'user.xml',
    ],
    'translation': [
    ],
}
