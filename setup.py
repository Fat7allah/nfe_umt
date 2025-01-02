from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="nfe_umt",
    version="0.0.1",
    description="نظام إدارة الجامعة الوطنية للتعليم",
    author="NFE",
    author_email="support@nfe.ma",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
