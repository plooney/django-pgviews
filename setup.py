from __future__ import absolute_import, print_function, unicode_literals

from setuptools import setup, find_packages

try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    LONG_DESCRIPTION = open('README.md').read()


setup(
    name='django-pgviews',
    version='0.5.1',
    description="Create and manage Postgres SQL Views in Django",
    long_description=LONG_DESCRIPTION,
    author='Scott Walton',
    author_email='scott.walton@mypebble.co.uk',
    license='Public Domain',
    packages=find_packages(),
    url='https://github.com/mypebble/django-pgviews',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ]
)
