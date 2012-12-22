Basicstrap style theme for Sphinx.

Features
========
* provide ``basicstrap`` theme for render HTML document.


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


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.
