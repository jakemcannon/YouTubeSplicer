
import os
import io
import sys

from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))
REQUIRED = [
    'ffmpeg',
    'youtube',
    'webvtt-py',
]

setup(name='youtubesplicer',
	packages=['youtubesplicer'],
	version='0.0.1',
	description='Automated video editing for cutting YouTube videos at interval where your keyword occurs.',
	author='Jacob Cannon',
	author_email='jakemcannon@gmail.com',
	license='MIT',
	url='https://github.com/jakemcannon/YouTubeSplicer',
	keywords=['youtube', 'video editing'],
	py_modules=['youtubesplicer'],
	entry_points={
		'console_scripts': ['youtubesplicer=youtubesplicer.youtubesplicer:main'],
	},

	install_requires=REQUIRED,
	include_package_data=True,
	classifiers=[
	'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

	],

	)