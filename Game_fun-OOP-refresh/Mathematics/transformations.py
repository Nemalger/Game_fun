from copy import copy
import yaml
from pprint import pprint
class Physics:

    def __init__(self):
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





