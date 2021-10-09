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
            plan = "",
            os = "",
            region = ""
        )

        with open("vultr-config.json", "w") as output:
            json.dump(data, output)