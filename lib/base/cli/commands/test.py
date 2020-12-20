from sploitkit import *


class test(Command):
    """ this is a test command """
    level = "module"
    single_arg = True

    def complete_values(self):
        #TODO: compute the list of possible values
        return ['test','test1']

    def run(self):
        print('this is a test command')
        #TODO: compute results here
        pass

    def validate(self, value):
        #TODO: validate the input value
        if value not in self.complete_values():
            raise ValueError("invalid value")

class test3(Command):
    """ this is a test command """
    level = "module"
    single_arg = True

    def complete_values(self):
        #TODO: compute the list of possible values
        return ['test','test3']

    def run(self,par1):
        print('this is a test command'+par1+'')
        #TODO: compute results here
        pass

    def validate(self, value):
        #TODO: validate the input value
        if value not in self.complete_values():
            raise ValueError("invalid value")


class test2(Command):
    """ Description here """
    level = "module"

    def complete_keys(self):
        #TODO: compute the list of possible keys
        return ['arg','arg','argument']

    def complete_values(self, key=None):
        #TODO: compute the list of possible values taking the key into account
        return ['test','test3']

    def run(self,par1):
        print('test2')
        print('this is a test command'+par1+'')


        #TODO: compute results here
        pass