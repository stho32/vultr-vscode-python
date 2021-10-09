"""
    This program is a friendly port of naseif/vultr-vscode .
    It creates a web vscode for you (and maybe for you and your coding buddies)
    so you can collaborate on a vultr vm.
"""
import argparse
from helpers.configuration import configuration

parser = argparse.ArgumentParser()

parser.add_argument("--init", action="store_true", help="create a new config file")
#parser.add_argument("--verbose", action="store_true", help="more output")

args = parser.parse_args()

if args.init:
    config = configuration()
    config.initialize()

