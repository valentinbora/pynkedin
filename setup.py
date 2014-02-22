from setuptools import setup, find_packages

requires_list = [
  'argparse>=1.2.1',
  'colorama>=0.2.5',
  'coverage>=3.6',
  'mock>=1.0.1',
  'nose>=1.3.0',
  'rauth>=0.6.2',
  'wsgiref>=0.1.2']

setup(name='pynkedin',
      version='1.0a',
      platforms='any',
      description='Python library for LinkedIn API',
      author='Vlad Temian, Valentin Bora',
      author_email='vladtemian@gmail.com, contact@valentinbora.com',
      url='https://github.com/valentinbora/pynkedin',
      packages = find_packages(),
      include_package_data=True,
      install_requires=requires_list,
      classifiers = [
        'Programming Language :: Python :: 2.7',
      ]
)
