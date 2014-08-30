from os import path
try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages

cwd = path.dirname(__file__)
__version__ = open(path.join(cwd, 'okfncart/okfncart_version.txt'),
                   'r').read().strip()

setup(
    name='okfncart',
    description='A simple shopping cart implementation',
    long_description=open('README.rst').read(),
    version=__version__,
    author='Tom Wardill',
    author_email='tom@howrandom.net',
    url='https://github.com/tomwardill/okfncart',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=open('requirements.txt').readlines(),
    package_data={'': ['okfn_version.txt', 'data.csv']},
    include_package_data=True,
    license='BSD',
    test_suite="okfncart.tests",
)