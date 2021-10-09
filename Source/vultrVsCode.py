"""
    This program is a friendly port of naseif/vultr-vscode .
    It creates a web vscode for you (and maybe for you and your coding buddies)
    so you can collaborate on a vultr vm.
"""
import argparse
from helpers.configuration import configuration
from vultr.create_instance import create_instance

parser = argparse.ArgumentParser()

parser.add_argument("--init", action="store_true", help="create a new config file")
parser.add_argument("--start", action="store_true", help="start vm and do all the things we need")
parser.add_argument("--stop", action="store_true", help="stop the vm and everything")

args = parser.parse_args()

config = configuration()

if args.init:
    config.initialize()

if args.start:
    vultr_config = config.load()
    print("Your VULTR API Key is: ")
    apiKey = input()
    print(create_instance(vultr_config["plan"], vultr_config["os"], vultr_config["region"], apiKey))

if args.stop:
    pass

