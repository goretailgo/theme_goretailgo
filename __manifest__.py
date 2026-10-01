{
    'name': 'GoRetailGo Theme',
    'version': '1.0',
    'category': 'Theme/Retail',
    'summary': 'Custom multi-tenant theme for GoRetailGo customer websites',
    'description': """
        Custom Odoo theme for GoRetailGo.
        Provides a dynamic, per-website product listing page that
        automatically renders using each tenant's own product data
        and branding, with a site-wide "Powered by GoRetailGo" strip.
    """,
    'author': 'GoRetailGo',
    'depends': ['website', 'website_sale'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_goretailgo/static/src/scss/theme.scss',
            'theme_goretailgo/static/src/js/theme.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
