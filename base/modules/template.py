from sploitkit import *

"""
class MyFirstModule(Module):
    \""" Description here 

    Author:  your name (your email)
    Version: 1.0
    \"""
    def run(self):
        pass
"""


class Procedure(Module):
    """ Description here 

    Author:  your name (your email)
    Version: 1.0
    """
    #groupId 			= ''
    #MetaModule.subcls.path = '/home/kali/'
    groups				= []	#Groups who have used this technique
    tactic  			= ''	#Tactic this technique belongs to
    techniqueId 		= ''	#Id of the Technique
    techniqueName 		= ''	#Name of the technique
    url					= ''	#URL of the MITRE page for the technique
    created				= ''	#Date the technique was created
    modified			= ''	#Date the technique was last modified
    sub_techiniques 	= []	#Subtechniques of this technique 

    def run(self):
        #self.get_modules("/home/kali/")
        pass
