"""
    create that new instance we want to use
"""
import requests
import time

def get_instance_update_for(id, apiKey):

    response = requests.get("https://api.vultr.com/v2/instances/" + id, headers={'Authorization': 'Bearer ' + apiKey})
    return response.json()

def create_instance(plan, os, region, apiKey):
    
    payload = dict(
        region = region,
        plan = plan,
        label = "VsCode",
        os_id = os
    )

    response = requests.post("https://api.vultr.com/v2/instances", headers={'Authorization': 'Bearer ' + apiKey}, json=payload)
    response_json = response.json()

    current_status = get_instance_update_for(response_json["instance"]["id"], apiKey)

    print("- creating vultr instance", flush=True, end="")

    while (current_status["instance"]["status"] == "pending"):
        time.sleep(3)
        current_status = get_instance_update_for(response_json["instance"]["id"], apiKey)
        print(".", end="", flush=True)

    print("")

    return dict(
        id = response_json["instance"]["id"],
        ip = current_status["instance"]["main_ip"],
        password = response_json["instance"]["default_password"]
    )