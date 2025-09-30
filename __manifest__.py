# -*- coding: utf-8 -*-
# Module: UI & Dashboard Management
# Provides dynamic UI components (icons, menus, views, dashboards, etc.)

# ████████╗ ██████╗██╗  ██╗███╗   ██╗ ██████╗     ███████╗███████╗███████╗
# ╚══██╔══╝██╔════╝██║  ██║████╗  ██║██╔═══██╗    ╚══███╔╝██╔════╝██╔════╝
#    ██║   ██║     ███████║██╔██╗ ██║██║   ██║      ███╔╝ █████╗  █████╗  
#    ██║   ██║     ██╔══██║██║╚██╗██║██║   ██║     ███╔╝  ██╔══╝  ██╔══╝  
#    ██║   ╚██████╗██║  ██║██║ ╚████║╚██████╔╝    ███████╗███████╗███████╗
#    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚══════╝╚══════╝                                              
{
    'name': "ZeeUI",

    'summary': "Dynamic UI and dashboard management for Odoo",
    'description': """
ZeeUI enhances the Odoo interface by providing a dynamic and customizable 
user experience. It includes configurable dashboards, icons, menus, and views 
that make navigation and management more intuitive.
    """,

    'author': "Techno Zee",
    'website': "https://github.com/Techno-Zee",
    'license': 'AGPL-3',
    'category': 'User Interface',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',  
    ],
    # External assets
    'assets': {
        'web.assets_backend': [
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
            'zee_ui/static/src/**/*.js',
            'zee_ui/static/src/**/*.css',
            'zee_ui/static/src/**/*.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

