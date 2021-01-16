#import procedure
from sploitkit import *
import pathlib 
import os,sys

#from procedure.procedure import Procedure

'''
class CommandWithOneArg(Command):
    """ Description here """
    level = "general"
    single_arg = True

    def complete_values(self):
        #TODO: compute the list of possible values
        return []

    def run(self):
        #TODO: compute results here
        pass

    def validate(self, value):
        #TODO: validate the input value
        if value not in self.complete_values():
            raise ValueError("invalid value")

class CommandWithTwoArgs(Command):
    """ Description here """
    level = "module"

    def complete_keys(self):
        #TODO: compute the list of possible keys
        return []

    def complete_values(self, key=None):
        #TODO: compute the list of possible values taking the key into account
        return []

    def run(self):
        #TODO: compute results here
        pass

'''

class reset(Command):
    """ Restart the console """
    level = "general"
    aliases = ["restart","reload"]
    def run(self):
        os.execl(sys.executable, sys.executable, * sys.argv)


class q(Command):
    """ Exit the console """
    level = "general"
    aliases = ["quit", "exit"]
          
    def run(self):
        raise ConsoleExit

class pwd(Command):
    """ Show current path """
    level = "general"

    def run(self):
        print(pathlib.Path(__file__).parent.absolute())

class ls(Command):
    level = "general"

    def run(self):
        os.system('ls -la')

class adversaries(Command):
    level = "general"

    def run(self):
        #print(Procedure.__subclasses__())
        pass



