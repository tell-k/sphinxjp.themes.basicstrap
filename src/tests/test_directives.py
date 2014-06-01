# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.basicstrap.directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import mock
import unittest


class FonticonRoleTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.basicstrap.directives import fonticon_role
        return fonticon_role

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        with mock.patch('sphinxjp.themes.basicstrap.directives.set_classes',
                        return_value=True, autospec=True) as mock_func:
            options = {}
            nodes, empty = self._callFUT(
                "name",
                "rawtext",
                "icon2 icon3",
                "lineno",
                "inliner",
                options=options,
            )
            mock_func.assert_called_with(options)
            self.assertEqual([], empty)
            self.assertEqual("icon", nodes[0]["classes"][0])
            self.assertEqual("icon2", nodes[0]["classes"][1])
            self.assertEqual("icon3", nodes[0]["classes"][2])


class SetupTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.basicstrap.directives import setup
        return setup

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyApp(object):

            def info(self, info):
                self.info = info

            def add_role(self, rolename, rolefunc):
                self.rolename = rolename
                self.rolefunc = rolefunc

        from sphinxjp.themes.basicstrap.directives import fonticon_role

        dummy_app = DummyApp()
        self._callFUT(dummy_app)
        self.assertEqual('Initializing Basicstrap theme directives',
                         dummy_app.info)
        self.assertEqual('fonticon', dummy_app.rolename)
        self.assertEqual(fonticon_role, dummy_app.rolefunc)
