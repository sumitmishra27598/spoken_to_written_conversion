import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken_to_written',
      packages = ['spoken_to_written'],
      version='0.1',
      description='Convert Spoken English given as text to Written English ',
      author='Sumit Mishra',
      author_email='sm27598@gmail.com',
      url='https://github.com/cyberdhiman/Spoken-To-Written-English',
      classifiers = ['Intended Audience :: Developers','Programming Language :: Python']
     )
