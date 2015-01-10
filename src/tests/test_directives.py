# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.basicstrap.directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import mock


class TestFonticonRole(object):

    def _get_target(self):
        from sphinxjp.themes.basicstrap.directives import fonticon_role
        return fonticon_role

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):

        with mock.patch('sphinxjp.themes.basicstrap.directives.set_classes',
                        return_value=True, autospec=True) as mock_func:
            options = {}
            nodes, empty = self._call_fut(
                "name",
                "rawtext",
                "icon2 icon3",
                "lineno",
                "inliner",
                options=options,
            )
            mock_func.assert_called_with(options)
            assert [] == empty
            assert "icon" == nodes[0]["classes"][0]
            assert "icon2" == nodes[0]["classes"][1]
            assert "icon3" == nodes[0]["classes"][2]


class TestSetup(object):

    def _get_target(self):
        from sphinxjp.themes.basicstrap.directives import setup
        return setup

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):

        class DummyApp(object):

            def info(self, info):
                self.info = info

            def add_role(self, rolename, rolefunc):
                self.rolename = rolename
                self.rolefunc = rolefunc

        from sphinxjp.themes.basicstrap.directives import fonticon_role

        dummy_app = DummyApp()
        self._call_fut(dummy_app)
        assert 'Initializing Basicstrap theme directives' == dummy_app.info
        assert 'fonticon' == dummy_app.rolename
        assert fonticon_role == dummy_app.rolefunc
