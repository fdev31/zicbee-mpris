#!/usr/bin/env python
import os
import sys
try:
	import setuptools
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
from setuptools import setup, find_packages

sys.path.insert(0, '.')
import zicbee_mpris
VERSION=zicbee_mpris.__version__

setup (
        name='zicbee-mpris',
        version=VERSION,
        author='Fabien Devaux',
        author_email='fdev31@gmail.com',
        url = 'http://zicbee.gnux.info/',
        download_url='http://zicbee.gnux.info:5000/zicbee-mpris/archive/%s.zip'%VERSION,
        license='BSD',
        platform='all',
        description='MPRIS backend for zicbee project',
        long_description='''Allow zicbee to use any MPRIS compatible player for playback''',
        keywords = 'database music tags metadata management mpris',
        packages = find_packages(),
        install_require = ['dbus-python'],

        entry_points = """
        [zicbee.player]
        mpris = zicbee_mpris.core:Player
        """,

        dependency_links = [
            'eggs',
            'http://zicbee.gnux.info/files/',
            'http://webpy.org/',
            'http://buzhug.sourceforge.net/',
            'http://code.google.com/p/quodlibet/downloads/list',
#            'http://sourceforge.net/project/showfiles.php?group_id=167078&package_id=190037&release_id=664931',
#            'http://code.google.com/p/pyglet/downloads/list',
            ],
        classifiers = [
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
#                'Intended Audience :: End Users/Desktop',
                'Operating System :: OS Independent',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'Environment :: Console',
                'Environment :: No Input/Output (Daemon)',
                'Environment :: X11 Applications',
                'Natural Language :: English',
                'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
                'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Topic :: Multimedia :: Sound/Audio :: Players',
                'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
                'Topic :: Text Processing :: Markup',
                'Topic :: Utilities',
                ],

        )

