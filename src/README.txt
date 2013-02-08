Basicstrap style theme for Sphinx.

Features
========
* provide ``basicstrap`` theme for render HTML document.
* using `Twitter Bootstrap <http://twitter.github.com/bootstrap/>`_.
* support Responsive Design.
* change the layout flexibility.
* `Google Web Fonts <http://www.google.com/webfonts>`_ available.
* `Font Awesome <http://fortawesome.github.com/Font-Awesome/>`_ available.
* easily change the design. by `Bootswatch <http://bootswatch.com/>`_.


Set up
======
Make environment with pip::

    $ pip install sphinxjp.themes.basicstrap

Make environment with easy_install::

    $ easy_install sphinxjp.themes.basicstrap


Convert Usage
=============
setup conf.py with::

    extensions = ['sphinxjp.themecore']
    html_theme = 'basicstrap'

and run::

    $ make html


Requirement
===========
* Python 2.7 or later (not support 3.x)
* Sphinx 1.1.x or later.
* sphinxjp.themecore 0.1.3 or later

Using
===========
* Twitter Bootstrap 2.2.2
* jQuery 1.8.3
* Bootswatch
* Font Awesome 3.0

License
=======
sphinxjp.themes.basicstrap Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .

Twitter Bootstrap is licensed under the `Apache license <https://github.com/twitter/bootstrap/blob/master/LICENSE>`_.

Bootswatch is licensed under the `Apache license <https://github.com/thomaspark/bootswatch/blob/gh-pages/LICENSE>`_.

Font Awesomeis licensed unde the `license <https://github.com/FortAwesome/Font-Awesome>`_.

* The Font Awesome font is licensed under the SIL Open Font License - http://scripts.sil.org/OFL
* Font Awesome CSS, LESS, and SASS files are licensed under the MIT License - http://opensource.org/licenses/mit-license.html
* The Font Awesome pictograms are licensed under the CC BY 3.0 License - http://creativecommons.org/licenses/by/3.0/

See the LICENSE file for specific terms.
