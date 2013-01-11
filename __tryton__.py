# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{
    'name': 'Nereid Party Multi User',
    'version': '2.4.0.3dev',
    'author': 'Openlabs Technologies & Consulting (P) Ltd.',
    'email': 'info@openlabs.co.in',
    'website': 'http://www.openlabs.co.in/',
    'description': '''
    Allow many to many relationship between party and nereid user

    see README for more information.
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
