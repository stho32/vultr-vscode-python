"""
    The things we need to do using SSH
"""
import os
import time
from fabric import Connection

class ssh:
    """
        ssh connection
    """
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        pass

    def execute(self, command):
        while True:
            try:
                print("  - run: " + command)
                result = Connection(self.ip, self.username, 
                    connect_kwargs={"password", self.password}).run(
                        command, 
                        hide=True)
                return result
            except:
                print("  - an error occured, retry in 3 seconds")
                time.sleep(3)

    def upload(self, localpath, remotepath):
        while True:
            try:
                print("  - upload: " + localpath + " > " + remotepath)
                result = Connection(self.ip, self.username,
                    connect_kwargs={"password", self.password}).put(
                        localpath, 
                        remote=remotepath
                    )
                return result
            except:
                print("  - an error occured, retry in 3 seconds")
                time.sleep(3)

