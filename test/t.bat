#!/bin/bash
cd ..
pip3 uninstall zas -y
pip3 install .
cd test
nosetests