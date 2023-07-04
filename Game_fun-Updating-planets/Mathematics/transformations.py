from copy import copy
import yaml
from pprint import pprint

from os.path import basename

import random
from collections import deque

import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
import numpy as np
npoints = 30
x = deque([0], maxlen=npoints)
y = deque([0], maxlen=npoints)
fig, ax = plt.subplots()
[line] = ax.step(x, y)

class Physics:

    def __init__(self):
        print(basename(""))
        with open('Mathematics/Config.YAML') as f:
            templates = yaml.safe_load(f)
        self.all_constants = templates['Base const']
        variable_parameters = templates['Variable parameters']
        self.functions = templates['Functions']
        for i in variable_parameters:
            self.all_constants[i] = eval(variable_parameters[i], copy(self.all_constants))

    def get_constant(self, name):
        return self.all_constants[name]

    def get_function(self, name_f, **argument):
        self.all_constants.update(argument)
        function = self.functions[name_f]
        return eval(function['formula'], self.all_constants)








