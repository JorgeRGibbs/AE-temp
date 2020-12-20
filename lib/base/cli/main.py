#!/usr/bin/python3
from sploitkit import FrameworkConsole


class MySploitConsole(FrameworkConsole):
    #TODO: set your console attributes
	attrib1 = 'test'
	attrib2 = 'saguaro'
	pass


if __name__ == '__main__':
    MySploitConsole(
        "AdversaryEmulator",
        #TODO: configure your console settings
    ).start()