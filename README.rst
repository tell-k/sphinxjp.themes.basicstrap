====================================================
sphinxjp.themes.basicstrap
====================================================

Basicstrap style theme for Sphinx. Using Twitter Bootstrap.

|travis| |coveralls| |downloads| |version| |license| |requires|

Features
========
* Provide ``basicstrap`` theme for render HTML document.
* Using `Twitter Bootstrap <http://twitter.github.com/bootstrap/>`_.
* Support Responsive Design.
* Change the layout flexibility.
* `Google Web Fonts <http://www.google.com/webfonts>`_ available.
* `Font Awesome <http://fortawesome.github.com/Font-Awesome/>`_ available.
* Easily change the design. by `Bootswatch <http://bootswatch.com/>`_.


Set up
======
Make environment with pip::

    $ pip install sphinxjp.themes.basicstrap

Convert Usage
=============
setup conf.py with::

    extensions += ['sphinxjp.themes.basicstrap']
    html_theme = 'basicstrap'

and run::

    $ make html

Requirement
===========
* Python 2.6, 2.7, 3.3, 3.4 or later.
* Sphinx 1.2.x or later.

Using
===========
* Twitter Bootstrap 3.3.4 and 2.3.2
* jQuery 1.11.1
* Bootswatch
* Font Awesome 4.3.0

License
=======

* sphinxjp.themes.basicstrap Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
* `Twitter Bootstrap is licensed under the Apache license <https://github.com/twitter/bootstrap/blob/master/LICENSE>`_.
* `Bootswatch is licensed under the Apache license <https://github.com/thomaspark/bootswatch/blob/gh-pages/LICENSE>`_.
* `Font Awesome is licensed under the license <https://github.com/FortAwesome/Font-Awesome>`_.
* `Geo is licensed under the license <https://github.com/divshot/geo-bootstrap>`_

See the LICENSE file for specific terms.

.. |travis| image:: https://travis-ci.org/tell-k/sphinxjp.themes.basicstrap.svg?branch=master
    :target: https://travis-ci.org/tell-k/sphinxjp.themes.basicstrap


.. |coveralls| image:: https://coveralls.io/repos/tell-k/sphinxjp.themes.basicstrap/badge.png
    :target: https://coveralls.io/r/tell-k/sphinxjp.themes.basicstrap
    :alt: coveralls.io

.. |downloads| image:: https://pypip.in/d/sphinxjp.themes.basicstrap/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.basicstrap/
    :alt: downloads

.. |version| image:: https://pypip.in/v/sphinxjp.themes.basicstrap/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.basicstrap/
    :alt: latest version

.. |license| image:: https://pypip.in/license/sphinxjp.themes.basicstrap/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.basicstrap/
    :alt: license

.. |requires| image:: https://requires.io/github/tell-k/sphinxjp.themes.basicstrap/requirements.svg?branch=master
    :target: https://requires.io/github/tell-k/sphinxjp.themes.basicstrap/requirements/?branch=master
    :alt: requires.io
