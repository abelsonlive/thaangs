import os
from setuptools import setup, find_packages

README = os.path.join(os.path.dirname(__file__), 'README.md')

REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')
REQUIREMENTS = open(REQUIREMENTS, 'r').read().splitlines()

VERSION = os.path.join(os.path.dirname(__file__), 'VERSION')
VERSION = open(VERSION, 'r').read().strip()


# setup
setup(
  name='thaangs',
  version=VERSION,
  description='The future of news.',
  long_description = README,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='',
  author='Brian Abelson',
  author_email='brian.abelson@voxmedia.com',
  url='http://github.com/abelsonlive/thaangs',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=REQUIREMENTS,
  entry_points={
      'console_scripts': [
          'fetch-thaangs = thaangs:fetch_all'
      ]
  },
  tests_require=['nose']
)