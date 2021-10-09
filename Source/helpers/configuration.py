"""
    Tools associated with the configuration
"""
import os
import json

class configuration:
    """
        provides access to the configuration
    """
    def __init__(self):
        pass

    def initialize(self):
        data = dict(
            plan = "vc2-4c-8gb",
            os = "387",
            region = "ams"
        )

        with open("vultr-config.json", "w") as output:
            json.dump(data, output)
    
    def load(self):
        with open("vultr-config.json") as inputfile:
            return json.load(inputfile)