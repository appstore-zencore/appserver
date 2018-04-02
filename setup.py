import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "six",
    "click",
    "pyyaml",
    "zdas",    
    "dictop",
    "magic_import",
]

setup(
    name="appstart",
    version="0.3.0",
    description="Application server framework help you write long run application.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/appstart",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['appstart'],
    requires=requires,
    install_requires=requires,
    packages=find_packages("src", exclude=["scripts"]),
    package_dir={"": "src"},
    scripts=["src/scripts/appserver",
             "src/scripts/appserver.py",
            ],
)