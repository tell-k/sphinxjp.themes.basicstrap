# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for basicstrap style'
copyright = u'2014, tell-k'

version = '0.4.2'

# -- Options for HTML output --------------------------

extensions = ['sphinxjp.themes.basicstrap']
html_theme = 'basicstrap'

# -- HTML theme options for `basicstrap` style -------

html_theme_options = {

    # Set the lang attribute of the html tag. Defaults to 'en'
    'lang': 'en',
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': False,
    # Show header searchbox. Defaults to false. works only "nosidber=True", 
    'header_searchbox': True,

    # Put the sidebar on the right side. Defaults to false.
    'rightsidebar': False,
    # Set the width of the sidebar. Defaults to 3
    'sidebar_span': 3,

    # Fix navbar to top of screen. Defaults to true
    'nav_fixed_top': True,
    # Fix the width of the sidebar. Defaults to false
    'nav_fixed': False,
    # Set the width of the sidebar. Defaults to '900px'
    'nav_width': '900px',
    # Fix the width of the content area. Defaults to false

    'content_fixed': False,
    # Set the width of the content area. Defaults to '900px'
    'content_width': '900px',
    # Fix the width of the row. Defaults to false
    'row_fixed': False,

    # Disable the responsive design. Defaults to false
    'noresponsive': False,
    # Disable the responsive footer relbar. Defaults to false
    'noresponsiverelbar': False,
    # Disable flat design. Defaults to false. Works only "bootstrap_version = 3"
    'noflatdesign': False,

    # Enable Google Web Font. Defaults to false
    'googlewebfont': False,
    # Set the URL of Google Web Font's CSS. Defaults to 'http://fonts.googleapis.com/css?family=Text+Me+One'
    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Lily+Script+One',  # NOQA
    # Set the Style of Google Web Font's CSS. Defaults to "font-family: 'Text Me One', sans-serif;"
    'googlewebfont_style': u"font-family: 'Lily Script One' cursive;",

    # Set 'navbar-inverse' attribute to header navbar. Defaults to false.
    'header_inverse': False,
    # Set 'navbar-inverse' attribute to relbar navbar. Defaults to false.
    'relbar_inverse': False,

    # Enable inner theme by Bootswatch. Defaults to false
    'inner_theme': True,
    # Set the name of innner theme. Defaults to 'bootswatch-simplex'
    'inner_theme_name': 'bootswatch-simplex',

    # Select Twitter bootstrap version 2 or 3. Defaults to '3'
    'bootstrap_version': '3',

    # Show "theme preview" button in header navbar. Defaults to false. 
    'theme_preview': True,

    # Set the Size of Heading text. Defaults to None
    # 'h1_size': '3.0em',
    # 'h2_size': '2.6em',
    # 'h3_size': '2.2em',
    # 'h4_size': '1.8em',
    # 'h5_size': '1.4em',
    # 'h6_size': '1.1em',
}
