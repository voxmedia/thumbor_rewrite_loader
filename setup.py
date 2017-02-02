# coding: utf-8

from setuptools import setup, find_packages

setup(
  name = 'thumbor_rewrite_loader',
  version = '0.9.0',
  description = 'Thumbor HTTP loader which rewrites matches from a list with a single canonical domain.',
  author = 'Jason Ormand',
  author_email = 'jason.ormand@voxmedia.com',
  url="https://github.com/voxmedia/thumbor_rewrite_loader",
  zip_safe = True,
  include_package_data = True,
  packages=find_packages(),
  classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python :: 2.7',
  ],
  install_requires=['thumbor>=5.2.0']
)