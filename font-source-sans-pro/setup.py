#!/usr/bin/env python

"""
Copyright (c) 2017 Pimoroni

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Text Processing :: Fonts']

setup(
    name            = 'font-source-sans-pro',
    version         = '0.0.1',
    author          = 'Philip Howard',
    author_email    = 'phil@pimoroni.com',
    description     = 'Source Sans Pro, sans-serif font',
    long_description= open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
    license         = 'SIL OFL 1.1',
    keywords        = 'Source Sans Pro Font',
    url             = 'https://github.com/pimoroni/fonts-python',
    classifiers     = classifiers,
    py_modules      = [],
    packages        = ['font_source_sans_pro'],
    package_data    = {'font_source_sans_pro': ['font_source_sans_pro/files']},
    entry_points    = {
        'fonts_ttf': [
            'sourcesansttf = font_source_sans_pro:font_files_ttf'
        ],
        'fonts_otf': [
            'sourcesansotf = font_source_sans_pro:font_files_otf'
        ]
    },
    zip_safe        = False,
    include_package_data = True
)
