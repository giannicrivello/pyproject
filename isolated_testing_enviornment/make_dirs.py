#! /bin/python

import pathlib


p = pathlib.Path('Parent/child1/child2')

p.mkdir(parents=True)
