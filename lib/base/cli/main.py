#!/usr/bin/python3
from sploitkit import FrameworkConsole, Config , Option


class MySploitConsole(FrameworkConsole):
	#TODO: set your console attributes
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
	#attrib1 = "module"
	pass


if __name__ == '__main__':
    MySploitConsole(
        "AdversaryEmulator",
        #TODO: configure your console settings
    ).start()