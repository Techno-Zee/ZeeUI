# -*- coding: utf-8 -*-
# Module: UI & Dashboard Management
# Provides dynamic UI components (icons, menus, views, dashboards, etc.)

# ████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗ ██████╗     ███████╗███████╗███████╗
# ╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██╔═══██╗    ╚══███╔╝██╔════╝██╔════╝
#    ██║   █████╗  ██║     ███████║██╔██╗ ██║██║   ██║      ███╔╝ █████╗  █████╗  
#    ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║   ██║     ███╔╝  ██╔══╝  ██╔══╝  
#    ██║   ███████╗╚██████╗██║  ██║██║ ╚████║╚██████╔╝    ███████╗███████╗███████╗
#    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚══════╝╚══════╝
                                                                                                                             
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
        # Security access control
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/dashboard_views.xml',
        'views/dashboard_block_views.xml',
        'views/dashboard_menu_views.xml',
        'views/dashboard_menu_inherit_views.xml',
        
        'wizard/dashboard_mail_views.xml', 
        
        # Menu & Actions
        'views/action.xml', 
        'views/menu.xml',
    ],
    # External assets
    'assets': {
        'web.assets_backend': [
            'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css',
            'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js',
            'https://cdn.jsdelivr.net/npm/interactjs/dist/interact.min.js',
            '//code.jquery.com/jquery-2.2.1.min.js',
            
            # Libraries 
            'zee_ui/static/lib/apexcharts/dist/apexcharts.min.js',
            'zee_ui/static/lib/jspdf/dist/jspdf.umd.min.js',
            'zee_ui/static/lib/gridstack/dist/gridstack-all.js',
            'zee_ui/static/lib/gridstack/dist/gridstack.min.css',
            
            'zee_ui/static/src/**/*.js',
            'zee_ui/static/src/**/*.css',
            'zee_ui/static/src/**/*.scss',
            'zee_ui/static/src/**/*.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        # 'demo/dashboard_theme.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

