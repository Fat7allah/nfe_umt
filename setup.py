from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nfe_umt/__init__.py
from nfe_umt import __version__ as version

setup(
    name="nfe_umt",
    version=version,
    description="نظام إدارة الجامعة الوطنية للتعليم",
    author="NFE",
    author_email="support@nfe.ma",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
