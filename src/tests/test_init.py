# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.basicstrap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import mock
import unittest


class GetPathTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.basicstrap import get_path
        return get_path

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from sphinxjp.themes import basicstrap
        self.assertEqual(basicstrap.template_path, self._callFUT())


class SetupTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.basicstrap import setup
        return setup

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        dummy_app = "dummy_app"

        with mock.patch('sphinxjp.themes.basicstrap.directives.setup',
                        return_value=True, autospec=True) as mock_func:

            self._callFUT(dummy_app)
            mock_func.assert_called_with(dummy_app)
