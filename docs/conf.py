# -*- coding: utf-8 -*-
#
# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for basicstrap style'
copyright = u'2014, tell-k'

version = '0.4.1'

# -- Options for HTML output ---------------------------------------------------

extensions = ['sphinxjp.themes.basicstrap']
html_theme = 'basicstrap'

# -- HTML theme options for `basicstrap` style -------------------------------------

html_theme_options = {
    'lang': 'en',
    'nosidebar': False,
    'rightsidebar': False,
    'sidebar_span': 3,
    'nav_fixed_top': True,

    'nav_fixed': False,
    'nav_width': '900px',

    'content_fixed': False,
    'content_width': '900px',

    'row_fixed': False,
    'noresponsive': False,
    'noflatdesign': False,

    'googlewebfont': False,
    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Lily+Script+One',
    'googlewebfont_style': u"font-family: 'Lily Script One' cursive;",

    'header_inverse': False,
    'relbar_inverse': False,

    'inner_theme': False,
    'inner_theme_name': 'bootswatch-flatly',

    'bootstrap_version': '3',
    'quick_preview': True,

    # 'h1_size': '3.0em',
    # 'h2_size': '2.6em',
    # 'h3_size': '2.2em',
    # 'h4_size': '1.8em',
    # 'h5_size': '1.4em',
    # 'h6_size': '1.1em',
}
