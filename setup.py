"""
<Here goes the module high-level description.

| author: Malek.Cellier@gmail.com
| created: 2022-11-25
"""


import os
import codecs
from setuptools import find_packages, setup

def readfile(name):
    """simple file reader"""
    with open(name, 'r') as fid:
        return fid.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

README = readfile('README.rst')
CHANGELOG = readfile('CHANGELOG.rst')

args = dict(
    name='pydrawtop',
    version=get_version('src/pydrawtop/__init__.py'),
    description='<describe your project here>',
    long_description=README + '\n\n' + CHANGELOG,
    python_requires='>=3.11',
    classifiers=[],
    url='',
    author='Malek Cellier',
    author_email='Malek.Cellier@gmail.com',
    keywords='',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    install_requires=readfile('requirements.txt').splitlines(),
    include_package_data=True,
    zip_safe=False
)

setup(**args)

