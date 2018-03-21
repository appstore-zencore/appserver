#!/bin/bash
cd ..
pip3 uninstall appserver -y
pip3 install .
cd test
nosetests