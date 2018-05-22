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
    "daemon_application",    
    "dictop",
    "magic_import",
]

setup(
    name="appserver",
    version="0.4.6",
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
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=['appserver'],
    scripts=["src/appserver.py"],
    entry_points={
        'console_scripts': ['appserver = appserver:server']
    },
)