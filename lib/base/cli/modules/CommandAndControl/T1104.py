from sploitkit import *
#from sploitkit import FrameworkConsole, Config , Option

class MultiStageChannels(Module):
	""" T1104

	Author:  your name (your email)
	Version: 1.0
	"""
	config  = Config({
	        Option(
	            'FILE',
	            "folder where application assets (i.e. logs) are saved",
	            True,
	            set_callback=lambda o: o.root._set_app_folder(),
	        ): "~/.{appname}",
	        Option(
	            'PDF',
	            "debug mode",
	            True,
	            bool,
	            set_callback=lambda o: o.root._set_logging(o.value),
	        ): "false",
	    })

	def run(self):
		pass

