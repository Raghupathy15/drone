# -*- coding: utf-8 -*-
{
    'name': "CRM",
    'summary': """ This module allowes to manage crm module """,
    'description': """
        This module allowes to manage CRM/Drone module
    """,

    'author': "Neoswis Technologies Dubai",
    'category': 'CRM',
    'version': '17.1',
    'depends': ['base'],
    

    'data': [

        'views/res_partner_views.xml',
        'security/ir.model.access.csv',

    ],
    'license': 'LGPL-3',
  
}

