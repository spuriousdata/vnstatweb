#!/usr/bin/env python
from setuptools import setup

setup(
    name='vnstatweb',
    version='0.2.0',
    description='Flask app for vnstati',
    license=open('LICENSE', 'r').read(),
    author="Mike O'Malley",
    author_email='spuriousdata at gmail dot com',
    url='http://github.com/spuriousdata/vnstatweb',
    install_requires=[
        'Flask >= 0.12',
        'flup >= 1.0',
    ],
    packages=[
        'vnstatweb',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
