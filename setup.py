from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['backtrace', 'colorama']

setup(
    name='xontrib-readable-traceback',
    version='0.2.5',
    description='Traceback easier to see for xonsh.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/6syun9/xontrib-readable-traceback',
    license='MIT',
    author='vaaaaanquish',
    author_email='6syun9@gmail.com',
    install_requires=install_requires,
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
)
