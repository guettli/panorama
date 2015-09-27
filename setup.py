from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='panorama',

    version='0.1',

    description='Create panorama in one run. Uses hugin for the real work.',

    url='https://github.com/guettli/panorama',

    # Author details
    author='Thomas Guettler',
    author_email='guettliml.panorama@thomas-guettler.de',

    license='Apache Software License',

    classifiers=[
        'Programming Language :: Python :: 2',
    ],

    entry_points={
        'console_scripts': [
            'create-panorama-from-jpg-files-in-directory=panorama.panorama:main',
        ],
    },
)
