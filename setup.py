from setuptools import setup
import os
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='panorama',

    version='0.1',

    description='Create panorama in one run. Uses hugin for the real work.',

    long_description=long_description,

    url='https://github.com/guettli/panorama',

    # Author details
    author='Thomas Guettler',
    author_email='guettliml.panorama@thomas-guettler.de',

    license='Apache Software License',

    install_requires=[
        'python-resize-image',
    ],

    classifiers=[
        'Programming Language :: Python :: 2',
    ],

    entry_points={
        'console_scripts': [
            'create-panorama-from-jpg-files-in-directory=panorama.panorama:main',
        ],
    },
)
