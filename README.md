# vultr-vscode-python
a python implementation of naseifs naseif/vultr-vscode which creates a web-vscode with an attached vultr vm

## initialize the configuration for vultr

First, we need to create a configuration file with some information
about the region, plan and vm-size:

```
vultrVsCode.sh --init
```

You can then modify the created vultr-config.json as you like.

## start the vm described in the configuration

```
vultrVsCode.sh --start
```

vultr vscode will ask you for the api key.
After that it will connect to vultr, create the instance as configured in the vultr-config.json.
