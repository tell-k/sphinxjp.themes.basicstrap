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

.. caution:: Caution when upgrading from 0.1.1 to 0.2.0

 * In version 0.1.1, the header color was black in the default, it has become white in 0.2.0. 
 * If you like the black color header, please set to True the 'header_inverse' option. 

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

* sphinxjp.themes.basicstrap Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
* `Twitter Bootstrap is licensed under the Apache license <https://github.com/twitter/bootstrap/blob/master/LICENSE>`_.
* `Bootswatch is licensed under the Apache license <https://github.com/thomaspark/bootswatch/blob/gh-pages/LICENSE>`_.
* `Font Awesome is licensed unde the license <https://github.com/FortAwesome/Font-Awesome>`_.

See the LICENSE file for specific terms.
