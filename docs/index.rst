=============================================
 Basicstrap style theme sample for Sphinx
=============================================


Quick preview inner theme
===========================

You can see the theme in real time If you select a theme.

.. raw:: html

 <a class="btn btn-lg btn-primary" href="#" data-toggle="modal" data-target=".debug-modal">launch quick preview window</a>


Quick start
===========

install(easy_install):

.. code-block:: bash

    $ easy_install sphinxjp.themes.basicstrap

install(pip):

.. code-block:: bash

    $ pip install sphinxjp.themes.basicstrap


setup your ``conf.py`` with:

.. code-block:: bash

    extensions = ['sphinxjp.themescore']
    html_theme = 'basicstrap'

and run:

.. code-block:: bash

    $ make html

then your will get this page's style HTML output.

In this document "inner_theme_name: bootswatch-flatly" is set. see also :ref:`sample_conf`


Links
=====

:download: https://github.com/tell-k/sphinxjp.themes.basicstrap
:repository: https://github.com/tell-k/sphinxjp.themes.basicstrap
:bug tracker: https://github.com/tell-k/sphinxjp.themes.basicstrap/issues


Contents
========

.. toctree::
    :maxdepth: 2

    readme
    options
    design
    sample
    history

