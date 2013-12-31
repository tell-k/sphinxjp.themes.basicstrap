# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.3.1'
long_description = '\n'.join([
        open(os.path.join("src", "README.txt")).read(),
        open(os.path.join("src", "AUTHORS.txt")).read(),
        open(os.path.join("src", "HISTORY.txt")).read(),
        ])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
    name='sphinxjp.themes.basicstrap',
    version=version,
    description='A sphinx theme for Basicstrap style. Using Twitter Bootstrap.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme'],
    author='tell-k',
    author_email='ffk2005 at gmail dot com',
    url='https://github.com/tell-k/sphinxjp.themes.basicstrap',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['buildout.cfg']},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'sphinx'
    ],
    test_suite='nose.collector',
    tests_require=['Nose','pep8'],
    extras_require=dict(test=['Nose','pep8']),
    entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.basicstrap:get_path

        [sphinx_directives]
        path = sphinxjp.themes.basicstrap:setup_directives
    """,
    zip_safe=False,
)
