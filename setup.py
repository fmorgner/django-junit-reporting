# pylint: disable=missing-docstring

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-junit_reporting',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='3-Clause BSD',
    description='A simple Django app to generate JUnit reports.',
    long_description=README,
    url='https://github.com/fmorgner/django-junit-reporting.git',
    author='Felix Morgner',
    author_email='felix.morgner@gmail.com',
    install_requires=[
        'Django',
        'djangorestframework',
        'junitparser',
        'django-font-awesome',
        'django-bootstrap3',
        'django-static-precompiler',
        'django-autoslug',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: 3-Clause BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
