# -*- coding: utf-8 -*-
import re
import os

from setuptools import setup, find_packages


here = os.path.dirname(__file__)

version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'src', 'sphinxjp',
                              'themes', 'basicstrap', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)

install_requires = [
    'setuptools',
    'Sphinx',
]

setup_requires = [
    "pytest-runner"
]

tests_require = [
    'pytest-cov',
    'pytest',
    'mock',
]

long_description = ""
with open(os.path.join(here, 'README.rst')) as fp:
    long_description = fp.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Framework :: Sphinx',
    'Framework :: Sphinx :: Extension',
    'Framework :: Sphinx :: Theme',
    'Topic :: Software Development',
    'Topic :: Software Development :: Documentation',
    'Topic :: Text Processing :: Markup',
]

setup(
    name='sphinxjp.themes.basicstrap',
    version=version,
    description='A sphinx theme for Basicstrap style. Using Twitter Bootstrap. #sphinxjp',  # NOQA
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme'],
    author='tell-k',
    author_email='ffk2005@gmail.com',
    url='https://github.com/tell-k/sphinxjp.themes.basicstrap',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'basicstrap = sphinxjp.themes.basicstrap',
        ]
    },
    zip_safe=False,
)
