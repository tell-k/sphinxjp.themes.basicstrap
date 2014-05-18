# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.basicstrap.directives
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from docutils import nodes
from docutils.parsers.rst.roles import set_classes


def fonticon_role(name, rawtext, text, lineno,
                  inliner, options={}, content=[]):
    """Create Font Icon Tag.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """
    set_classes(options)
    options['classes'] = ["icon"]
    for icon in text.split(" "):
        options['classes'].append(icon)
    return [nodes.inline('', '', **options)], []


def setup(app):
    """Initialize
    :param app: Sphinx application context.
    """
    app.info('Initializing Basicstrap theme directives')
    app.add_role('fonticon', fonticon_role)
    return
