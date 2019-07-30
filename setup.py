#coding: utf-8

from setuptools import setup, find_packages


# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='ROBOT',
      version="0.0.1",
      description="",
      url="https://github.com/ymussi/p4c_robot.git",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords="robot p4c",
      packages=find_packages(),
      package_data={'robot.parsers': ['*/*.json', '*/*xml']},
      zip_safe=False
      ),
