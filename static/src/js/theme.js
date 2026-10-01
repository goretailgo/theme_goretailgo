// GoRetailGo Theme - frontend JS

// The top white navbar always shows the GoRetailGo platform logo
// (same on every tenant site, like Amazon's own logo on a seller page).
// Per-tenant branding shows instead in the navy hero banner below it.
// Selector is broad + excludes our own hero/strip logos, since Odoo's
// exact header markup varies by version/theme.
function grgFixNavbarLogo() {
    var headers = document.querySelectorAll('header#top, .o_header_standard, #o_main_nav');
    headers.forEach(function (header) {
        header.querySelectorAll('img').forEach(function (img) {
            if (img.classList.contains('grg-hero-logo') || img.classList.contains('grg-powered-logo')) {
                return;
            }
            img.setAttribute('src', '/theme_goretailgo/static/src/img/logo.png');
            img.setAttribute('alt', 'GoRetailGo');
        });
    });
}

document.addEventListener('DOMContentLoaded', grgFixNavbarLogo);
window.addEventListener('load', grgFixNavbarLogo);
setTimeout(grgFixNavbarLogo, 500);
