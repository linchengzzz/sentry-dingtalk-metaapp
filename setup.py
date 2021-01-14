# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
from setuptools import setup, find_packages

NAME = 'sentry-dingtalk-metaapp'
AUTHOR = 'Linchengzzz'
EMAIL = '1139489076@qq.com'
VERSION = '1.0.13'
DESCRIPTION = 'sentry extension which can send error to ding-talk.'
URL = 'https://github.com/linchengzzz/sentry-dingtalk-metaapp'
LICENSE = 'GPL License'
KEYWORDS = 'Sentry DingTalk MetaApp'

INSTALL_REQUIRES = [
    'sentry',
    'requests',
    'Django',
]

try:
    with io.open(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                'README.md'
            ),
            encoding='utf-8'
    ) as f:
        LONG_DESCRIPTION = '\n' + f.read()
except Exception as exception:
    del exception
    LONG_DESCRIPTION = DESCRIPTION
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,

    url=URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    license=LICENSE,
    keywords=KEYWORDS,

    include_package_data=True,
    zip_safe=False,

    package_dir={'': 'src'},
    packages=find_packages('src'),

    tests_require=INSTALL_REQUIRES,
    install_requires=INSTALL_REQUIRES,

    entry_points={
        'sentry.plugins': [
            'sentry_dingtalk_metaapp = sentry_dingtalk_metaapp.plugin:DingTalkPlugin'
        ]
    },

    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ]
)
