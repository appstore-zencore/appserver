import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "click",
    "pyyaml",
    "dictop",
    "zdas",
    "zencore_utils",
]

setup(
    name="appserver",
    version="0.2.0",
    description="Application server framework help you write long run application.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/appserver",
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
    keywords=['appserver'],
    requires=requires,
    install_requires=requires,
    packages=find_packages("src", exclude=["scripts"]),
    package_dir={"": "src"},
    scripts=["src/scripts/apprun",
             "src/scripts/apprun.py",
            ],
)