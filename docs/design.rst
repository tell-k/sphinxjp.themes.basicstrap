========================
 Customize the design
========================

By setting the html_theme_options in your conf.py, you can change the look and feel some flexibility.
Because it contains an example of a simple configuration, please try to be helpful.


Sidebar Layout
========================

If you want to place sidebar to the right, please change "rightsidebar" option.

Right Sidebar
-------------------------------

::

  html_theme_options = {
      'rightsidebar': True,
  }

.. figure:: _static/img/h7nd8z~ym33s.png
   :width: 50%

   Figure1: rightsidebar

Change Sidebar Width
-------------------------------

If you want to change the width of the sidebar, please change "sidebar_span" option.

Using `a Grid system of Twitter Bootstrap <http://twitter.github.com/bootstrap/scaffolding.html#gridSystem>`_.

::

  html_theme_options = {
      'sidebar_span': 6, # 1(min) 〜 12(max)
  }

.. figure:: _static/img/c5tpwcsivlxs.png
   :width: 50%

   Figure2: sidebar-span

No Sidebar
-------------------------------

Fixed Layout
========================


fixed Navbar
-----------------------------

fixed Content Area
-----------------------------

Inverse Color
========================

Responsive Design
========================

Inner Design Theme
========================

Web Font
========================

Font Icon
========================
