# -*- coding: utf-8 -*-
{
    'name': "exe_pos_srkiosquero",

    'summary': """
        oculta botones en pos""",

    'description': """
        Customizacion SrKiosquero oculta botones en pos
    """,

    'author': "Exemax, apigaby",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['pos','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode

}
