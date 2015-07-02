#!/usr/bin/env python

import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'requests',
    'requests.packages',
    'requests.packages.chardet',
    'requests.packages.urllib3',
    'requests.packages.urllib3.packages',
    'requests.packages.urllib3.contrib',
    'requests.packages.urllib3.util',
    'requests.packages.urllib3.packages.ssl_match_hostname',
]

requires = []

version = ''
with open('requests/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='vecpy',
    version=version,
    description='Simple Vector package to help with basic linear algebra.',
    long_description=readme + '\n\n' + history,
    author='Jonas I. Liechti',
    author_email='jon.liechti@gmail.com',
    url='http://python-requests.org',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'vecpy': 'vecpy'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent'
    ),
    # dependency_links = [
    #     "http://..."
    # ],
)
