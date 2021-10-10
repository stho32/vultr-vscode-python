"""
    This program is a friendly port of naseif/vultr-vscode .
    It creates a web vscode for you (and maybe for you and your coding buddies)
    so you can collaborate on a vultr vm.
"""
import argparse
import os
from posixpath import abspath
from helpers.ssh import ssh
from helpers.configuration import configuration
from vultr.create_instance import create_instance

parser = argparse.ArgumentParser()

parser.add_argument("--init", action="store_true", help="create a new config file")
parser.add_argument("--start", action="store_true", help="start vm and do all the things we need")
parser.add_argument("--stop", action="store_true", help="stop the vm and everything")

args = parser.parse_args()

config = configuration()
currentDirectory = os.path.dirname(os.path.abspath(__file__))
installscript = os.path.abspath(os.path.join(currentDirectory, "../setup-files-for-vms/install.sh"))
installscript_target = "/root/install.sh"
code_server_config = os.path.abspath(os.path.join(currentDirectory, "../setup-files-for-vms/code-server"))
code_server_config_target = "/root/code-server"

if args.init:
    config.initialize()

if args.start:
    # grab config
    vultr_config = config.load()

    # get api key from user
    print("Your VULTR API Key is: ")
    apiKey = input()

    # create the instance and wait for it to come up
    instance = create_instance(vultr_config["plan"], vultr_config["os"], vultr_config["region"], apiKey)

    connection = ssh(instance["ip"], "root", instance["password"])
    print(instance)

    connection.execute("uname -a")
    connection.upload(installscript, installscript_target)
    connection.upload(code_server_config, code_server_config_target)

    print(instance)

if args.stop:
    pass

