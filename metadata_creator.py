import json

huns = 0
tens = 0
release = "Life Seeking Darkness"
path = "/home/gneale/Pictures/nft-sf/life_seeking_darkness/"

def print_json(dict):
    print(json.dumps(dict, sort_keys=True, indent=4))

for num in range (200,300):
    if num < 10:
        x = "{}{}{}".format(huns, tens, num)
    elif num < 100:
        x = "{}{}".format(huns, num) 
    else:
        x = "{}".format(num)   
    
    md = {
    "series_number": num,
    "series_total": 726,
    "format":"CHIP-0007",
    "name": x,
    "description": "Original work by Gerald Neale for chia.",
    "minting_tool": "CLI",
    "sensitive_content": "false",
    "attributes":[
        {"trait_type": "Artist", "value": "Gerald Dominic Neale"},
        {"trait_type": "Release", "value": release}],
    "collection": {
        "id": "6efc444d-3b30-4e7f-be74-a679bad5131c",
        "name": "San Francisco by Gerald Neale",
    "attributes": [
        {"type": "description", "value": "Dramatic topography meets hyper-manifested initiatives."},
        {"type": "icon", "value": "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco4.png"},
        {"type": "banner", "value": "https://mojopuzzler.org/nft/gnsf/gneale-san_francisco4.png"},
        {"type": "github", "value": "https://github.com/geraldneale"},
        {"type": "website", "value": "https://mojopuzzler.org"},
        {"type": "twitter", "value": "https://twitter.com/GeraldNeale"},
        {"type": "discord", "value": "https://discord.com/invite/JcSxVBzJyB"},
        {"type": "representation", "value": "bigday@bigdayfilmcollective.com"}
    ]
    }
    }

    print_json(md)
    #write to file for reference
    fname = "gneale-san_francisco{}.json".format(num)
    with open(path + fname, 'w') as outfile:
        json.dump(md, outfile, sort_keys=True, indent=4)
