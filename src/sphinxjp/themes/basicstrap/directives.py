# -*- coding: utf-8 -*-
"""
    publishers.account.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: teruhiko kida <teruhiko.kida@beproud.jp>
    :copyright: Be Proud Inc. All Rights Reserved.
"""
from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes

def fonticon_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Link to a BitBucket issue.

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """

    #app.info('issue %r' % text)
    set_classes(options)
    options['classes']=["icon"]
    for icon in text.split(" "):
        options['classes'].append(icon)
    node = nodes.inline('', '', **options)
    return [node], []

def setup(app):
    """Initialize

    :param app: Sphinx application context.
    """
    app.info('Initializing Basicstrap theme directives')
    app.add_role('fonticon', fonticon_role)
    return

