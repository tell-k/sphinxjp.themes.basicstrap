====================================================
 Sample Document
====================================================

.. contents::
   :local:


Admonitions (Docutils origin)
===============================================================================

.. danger::
   This is sample of admonition directive for "Danger".

.. error::
   This is sample of admonition directive for "Error".

.. warning::
   This is sample of admonition directive for "Warning".

.. caution::
   This is sample of admonition directive for "Caution".

.. attention::
   This is sample of admonition directive for "Attention".

.. important::
   This is sample of admonition directive for "Important".

.. note::
   This is sample of admonition directive for "Note".

.. hint::
   This is sample of admonition directive for "Hint".

.. tip::
   This is sample of admonition directive for "Tip".


Admonitions (Sphinx Additional)
===============================

.. seealso::
   This is sample of admonition directive for "SeeAlso".

.. versionadded:: 0.3.1
   Here is description of specification which added on that version.

.. versionchanged:: 0.8
   Here is description of specification which changed on that version.

.. code-block:: python

   >>> from fibo import fib, fib2
   >>> fib(500)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377


Headings
========
This is a first level heading (``h1``).

Sub-Heading
-----------
This is a second level heading (``h2``).

Sub-Sub-Heading
~~~~~~~~~~~~~~~
This is a third level heading (``h3``).


Code
====
The Sphinx Bootstrap Theme uses Bootstrap styling for ``inline code text`` and
::

    multiline
    code text

Here's an included example with line numbers.

.. literalinclude:: ../../sphinx_bootstrap_theme/__init__.py
   :linenos:

It also works with existing Sphinx highlighting:

.. code-block:: html

    <html>
      <body>Hello World</body>
    </html>

.. code-block:: python

    def hello():
        """Greet."""
        return "Hello World"

.. code-block:: javascript

    /**
     * Greet.
     */
    function hello(): {
      return "Hello World";
    }


Footnotes
=========
I have footnoted a first item [#f3]_ and second item [#f4]_.

.. rubric:: Footnotes
.. [#f3] My first footnote.
.. [#f4] My second footnote.

Citation
========

Citation references, like [CIT2002]_.
Note that citations may get
rearranged, e.g., to the bottom of
the "page".

Citation labels contain alphanumerics,
underlines, hyphens and fullstops.
Case is not significant.

Given a citation like [this]_, one
can also refer to it like this_.


.. [CIT2002] A citation
   (as often used in journals).
.. [this] here.

Comments
========

An "empty comment" does not
consume following blocks.
(An empty comment is ".." with
blank lines before and after.)
..

        So this block is not "lost",
        despite its indentation.

Tables
======

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

::

 +------------------------+------------+----------+----------+
 | Header row, column 1   | Header 2   | Header 3 | Header 4 |
 | (header rows optional) |            |          |          |
 +========================+============+==========+==========+
 | body row 1, column 1   | column 2   | column 3 | column 4 |
 +------------------------+------------+----------+----------+
 | body row 2             | ...        | ...      |          |
 +------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

::

  =====  =====  =======
  A      B      A and B
  =====  =====  =======
  False  False  False
  True   False  False
  False  True   False
  True   True   True
  =====  =====  =======

.. csv-table:: CSV Table
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

::

  .. csv-table:: CSV Table
     :header: "Treat", "Quantity", "Description"
     :widths: 15, 10, 30

     "Albatross", 2.99, "On a stick!"
     "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
     crunchy, now would it?"
     "Gannet Ripple", 1.99, "On a stick!"

.. list-table:: List Table
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

::

  .. list-table:: List Table
     :widths: 15 10 30
     :header-rows: 1

     * - Treat
       - Quantity
       - Description
     * - Albatross
       - 2.99
       - On a stick!
     * - Crunchy Frog
       - 1.49
       - If we took the bones out, it wouldn't be
         crunchy, now would it?
     * - Gannet Ripple
       - 1.99
         - On a stick!

Grid
----
A "**bordered**" grid table:

.. cssclass:: table-bordered

+------------------------+------------+----------+----------+
| Header1                | Header2    | Header3  | Header4  |
+========================+============+==========+==========+
| row1, cell1            | cell2      | cell3    | cell4    |
+------------------------+------------+----------+----------+
| row2 ...               | ...        | ...      |          |
+------------------------+------------+----------+----------+
| ...                    | ...        | ...      |          |
+------------------------+------------+----------+----------+

which uses the directive::

    .. cssclass:: table-bordered

Simple
------
A simple "**striped**" table:

.. cssclass:: table-striped

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

which uses the directive::

    .. cssclass:: table-striped

And a "**hoverable**" table:

.. cssclass:: table-hover

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

which uses the directive::

    .. cssclass:: table-hover

Mix
------

.. cssclass:: table-bordered table-striped table-hover

+------------------------+------------+----------+----------+
| Header1                | Header2    | Header3  | Header4  |
+========================+============+==========+==========+
| row1, cell1            | cell2      | cell3    | cell4    |
+------------------------+------------+----------+----------+
| row2 ...               | ...        | ...      |          |
+------------------------+------------+----------+----------+
| ...                    | ...        | ...      |          |
+------------------------+------------+----------+----------+

which uses the directive::

    .. cssclass:: table-bordered table-striped table-hover
