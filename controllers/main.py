from odoo import http
from odoo.http import request


class GoRetailGoWebsite(http.Controller):

    @http.route('/shop-custom', type='http', auth='public', website=True)
    def custom_shop_page(self, **kwargs):
        website = request.website
        products = request.env['product.template'].sudo().search([
            ('website_id', 'in', [False, website.id]),
            ('is_published', '=', True),
        ])
        return request.render('theme_goretailgo.custom_shop_template', {
            'products': products,
            'website': website,
        })
