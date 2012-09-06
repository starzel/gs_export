#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='gs_export',
    version='0.1.0',
    author='Patrick Gerken',
    author_email='gerken@patrick-gerken.de',
    url='https://github.com/starzel/gs_export',
    description='A little shell script to dump you GenericSetup profile somewhere and notify you for changes'
        ,
    long_description=open('README.txt').read() + '''

'''
        + open('CHANGES.txt').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        ],
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    install_requires=['outbox'],
    package_dir={'': 'src'},
    packages=['gs_export'],
    entry_points={'console_scripts': ['gs_export=gs_export:main']},
    )
