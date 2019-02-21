#!/usr/bin/env python
from setuptools import setup, find_packages

#setup(name="nhs_code_test", packages=find_packages())



setup(name="nhs_code_test",
      version="0.0.1",
      description="""Coding test""",
      author='Giovanni Bronzini',
      author_email='g.bronzini@gmail.com',
      url='https://github.com/GigiusB/coding_test_1',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'news_search = nhs.cli:main',
          ],
      },
      install_requires=[
          'Click',
      ],
      license='MIT',
      zip_safe=False,
      keywords='',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6'
      ])
