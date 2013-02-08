# -*- coding: utf-8 -*-
#
# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for basicstrap style'
copyright = u'2012, tell-k'

version = '0.1.0'

# -- Options for HTML output ---------------------------------------------------

extensions = ['sphinxjp.themecore']
html_theme = 'basicstrap'

# -- HTML theme options for `dotted` style -------------------------------------

html_theme_options = {
    'lang': 'en',
    'nosidebar': False,
    'rightsidebar': False,
    'sidebar_span': 3,
    'nav_fixed': False,
    'nav_width': '900px',
    'content_fixed': False,
    'content_width': '900px',
    'row_fixed': False,
    'noresponsive': False,
    'googlewebfont': False,
    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Text+Me+One',
    'googlewebfont_style': "font-family: 'Text Me One', sans-serif",
    'header_inverse': False,
    'relbar_inverse': False,
    'inner_theme': False,
    'inner_theme_name': 'bootswatch-united',
}
