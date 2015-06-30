#!/usr/bin/env python

from __future__ import print_function

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

VERSION = __import__("whatsapp_secretary").__version__

CLASSIFIERS = [

    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development',

    # Pick your license as you wish (should match "license" above)
    'License :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7'
]

INSTALL_REQUIRES = [

    'yowsup2>=2.3.123'

]

EXTRA_REQUIRES = {

    'dev': ['ipython>=3.2.0', 'ipdb>=0.8.1'],
    'test': ['pytest>=2.7.2'],
}

setup(
    name="whatsapp-secretary",
    description="Tell your whatsapp secretary to let you know just that what\'s actually important for you.",
    license='MIT',
    version=VERSION,
    author='Zuri Pabon',
    author_email='zurisadai.pabon@gmail.com',
    url='https://github.com/Tsur/whatsapp-secretary',
    download_url="https://github.com/Tsur/whatsapp-secretary/archive/master.zip",
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    platforms='any',
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRES,
    classifiers=CLASSIFIERS,
    scripts=['whatsapp-secretary']
)
