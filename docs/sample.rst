====================================================
 Sample Document
====================================================

.. contents::
   :local:


Admonitions (Docutils origin)
==============================

.. danger::
   This is sample of admonition directive for "Danger".

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

   .. code-block:: python
      :linenos:

      >>> from fibo import fib, fib2
      >>> fib(500)
      1 1 2 3 5 8 13 21 34 55 89 144 233 377

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

.. code-block:: python
   :linenos:

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
     **/
    function hello(): {
      return "Hello World";
    }


Footnotes
=========
I have footnoted a first item [#f3]_ and second item [#f4]_.

.. rubric:: Footnotes
.. [#f3] My first footnote.
.. [#f4] My second footnote.

.. [1] A footnote contains body elements, consistently indented by at
   least 3 spaces.

   This is the footnote's second paragraph.

.. [#label] Footnotes may be numbered, either manually (as in [1]_) or
   automatically using a "#"-prefixed label.  This footnote has a
   label so it can be referred to from multiple places, both as a
   footnote reference ([#label]_).

.. [#] This footnote is numbered automatically and anonymously using a
   label of "#" only.

.. [*] Footnotes may also use symbols, specified with a "*" label.
   Here's a reference to the next footnote: [*]_.

.. [*] This footnote shows the next symbol in the sequence.


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
---

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


Structural Elements
===================

Section Title
-------------

That's it, the text just above this line.

Transitions
-----------

Here's a transition:

---------

It divides the section.

Body Elements
=============

Paragraphs
----------

A paragraph.

Bullet Lists
------------

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

Enumerated Lists
----------------

1. Arabic numerals.

   a) lower alpha)

      (i) (lower roman)

          A. upper alpha.

             I) upper roman)

2. Lists that don't start at 1:

   3. Three

   4. Four

   C. C

   D. D

   iii. iii

   iv. iv

#. List items may also be auto-enumerated.

Definition Lists
----------------

Term
    Definition
Term : classifier
    Definition paragraph 1.

    Definition paragraph 2.
Term
    Definition

Field Lists
-----------

:what: Field lists map field names to field bodies, like database
       records.  They are often part of an extension syntax.  They are
       an unambiguous variant of RFC 2822 fields.

:how arg1 arg2:

    The field marker is a colon, the field name, and a colon.

    The field body may contain one or more body elements, indented
    relative to the field marker.

Option Lists
------------

For listing command-line options:

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments

--very-long-option
              The description can also start on the next line.

              The description may contain multiple body elements,
              regardless of where it starts.

-x, -y, -z    Multiple options are an "option group".
-v, --verbose  Commonly-seen: short & long options.
-1 file, --one=file, --two file
              Multiple options with arguments.
/V            DOS/VMS-style options too

There must be at least two spaces between the option and the
description.

Literal Blocks
--------------

Literal blocks are indicated with a double-colon ("::") at the end of
the preceding paragraph (over there ``-->``).  They can be indented::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Or they can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?

Line Blocks
-----------

| This is a line block.  It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
  they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

Block Quotes
------------

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Doctest Blocks
--------------

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)

Directives
----------

.. contents:: :local:

These are just a sample of the many reStructuredText Directives.  For
others, please see
http://docutils.sourceforge.net/docs/ref/rst/directives.html.

Topics, Sidebars, and Rubrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Sidebar Title
   :subtitle: Optional Subtitle

   This is a sidebar.  It is for text outside the flow of the main
   text.

   .. rubric:: This is a rubric inside a sidebar

   Sidebars often appears beside the main text with a border and
   background color.

.. topic:: Topic Title

   This is a topic.

.. rubric:: This is a rubric

Compound Paragraph
~~~~~~~~~~~~~~~~~~

.. compound::

   This paragraph contains a literal block::

       Connecting... OK
       Transmitting data... OK
       Disconnecting... OK

   and thus consists of a simple paragraph, a literal block, and
   another simple paragraph.  Nonetheless it is semantically *one*
   paragraph.

This construct is called a *compound paragraph* and can be produced
with the "compound" directive.

Comments
--------

Here's one:

.. Comments begin with two dots and a space. Anything may
   follow, except for the syntax of footnotes, hyperlink
   targets, directives, or substitution definitions.

   Double-dashes -- "--" -- must be escaped somehow in HTML output.

(View the HTML source to see the comment.)

Admonitions with inner blocks
=============================

.. tip::
   This is sample of admonition directive for "Tip" with a bullet list

   * list item A
   * list item B
   * list item C

.. tip::
   This is sample of admonition directive for "Tip" with a numbered list

   1) list item 1
   2) list item 2
   3) list item 3

.. tip::
   This is sample of admonition directive for "Tip" with a definition list

   Term
       Definition
   Term : classifier
       Definition paragraph 1.

       Definition paragraph 2.
   Term
       Definition


.. tip::
   This is sample of admonition directive for "Tip" with a code

   .. code-block:: none

      single line of code without line numbers

.. tip::
   This is sample of admonition directive for "Tip" with a code with line numbers
.. code-block:: none
      :linenos:

      line 1
      line 2

.. tip::
   This is sample of admonition directive for "Tip" with a table

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. tip::
   This is sample of admonition directive for "Tip" with a block quote

       My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
       as follows and begins now.  All brontosauruses are thin at one
       end, much much thicker in the middle and then thin again at the
       far end.  That is my theory, it is mine, and belongs to me and I
       own it, and what it is too.

       -- Anne Elk (Miss)

.. note::
   This is sample of admonition directive for "Note" with a table

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. note::
   This is sample of admonition directive for "Note" with a block quote

       My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
       as follows and begins now.  All brontosauruses are thin at one
       end, much much thicker in the middle and then thin again at the
       far end.  That is my theory, it is mine, and belongs to me and I
       own it, and what it is too.

       -- Anne Elk (Miss)

.. warning::
   This is sample of admonition directive for "Warning" with a table

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. warning::
   This is sample of admonition directive for "Warning" with a block quote

       My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
       as follows and begins now.  All brontosauruses are thin at one
       end, much much thicker in the middle and then thin again at the
       far end.  That is my theory, it is mine, and belongs to me and I
       own it, and what it is too.

       -- Anne Elk (Miss)

.. error::
   This is sample of admonition directive for "Error" with a table

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. error::
   This is sample of admonition directive for "Error" with a block quote

       My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
       as follows and begins now.  All brontosauruses are thin at one
       end, much much thicker in the middle and then thin again at the
       far end.  That is my theory, it is mine, and belongs to me and I
       own it, and what it is too.

       -- Anne Elk (Miss)

.. admonition::
   This is sample of admonition directive for "Admonition" with a table

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

.. admonition::
   This is sample of admonition directive for "Admonition" with a block quote

       My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
       as follows and begins now.  All brontosauruses are thin at one
       end, much much thicker in the middle and then thin again at the
       far end.  That is my theory, it is mine, and belongs to me and I
       own it, and what it is too.

       -- Anne Elk (Miss)



Headings
========

Display line numbers:

.. code-block:: html
   :linenos:

    <html>
      <body>Hello World</body>
    </html>

Long lines
----------

Here are very long lines with

.. code-block:: none

   A very very very, really very very lery, really really very, super mega giga long long very long absurd long line of text with even more text comming after this full-stop . Told ya! More and more and more.

with line numbers

.. code-block:: none
   :linenos:

   A very very very, really very very lery, really really very, super mega giga long long very long absurd long line of text with even more text comming after this full-stop . Told ya! More and more and more.

with line numbers and caption

.. code-block:: none
   :caption: A caption
   :linenos:

   A very very very, really very very lery, really really very, super mega giga long long very long absurd long line of text with even more text comming after this full-stop . Told ya! More and more and more.

