from setuptools import setup, find_packages

setup(
      version='1.0',
      author='Koshmanov Nikita INC',
      packages=find_packages(),
      install_requires=[
          'Django==3.0.5',
          'djangorestframework==3.11.0',
          'gunicorn==20.0.4',
          'psycopg2==2.8.5'
      ],
)