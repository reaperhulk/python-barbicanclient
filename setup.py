#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Copyright (c) 2013 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import setuptools

name = 'python-barbicanclient'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name=name,
    version="0.1dev",
    description='Client Library for OpenStack Barbican Key Management API',
    long_description=read('README.md'),
    keywords="openstack encryption key-management secret",
    url='https://github.com/cloudkeep/barbican',
    license='Apache License (2.0)',
    author='OpenStack, LLC.',
    author_email='openstack-admins@lists.launchpad.net',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*']),
    install_requires=[
        'eventlet>=0.12.1',
        'httplib2>=0.7.7',
        'argparse>=1.2.1',
        'python-keystoneclient>=0.2.3',
        'iso8601>=0.1.4'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: OpenStack',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts = ['keep']
)
