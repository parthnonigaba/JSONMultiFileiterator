import json

# Open the JSON file

import json
import re
import base64

list = []

def base64_to_hex(base64_str):
    # Decode the Base64 string to bytes
    decoded_bytes = base64.b64decode(base64_str)
    
    # Convert the bytes to a hex string
    hex_str = decoded_bytes.hex()
    
    return hex_str

# Example usage



pattern = re.compile(r"/mwg/\s*-\s*Memetic\s+Warfare\s+General", re.IGNORECASE)

with open("/Users/parthgaba/Desktop/Twitter/4plebs_data/April_file", "r") as f:
    for line in f:
        data = json.loads(line)
        
        for key in data.keys():
            if(key=='sub'):
                if(re.search(pattern,data.get(key)) != None):
                    base64_str = data.get("md5")  
                    hex_str = base64_to_hex(base64_str)
                    list.append(hex_str)
with open("/Users/parthgaba/Desktop/Twitter/4plebs_data/May_file", "r") as f:
    for line in f:
        data = json.loads(line)
        
        for key in data.keys():
            if(key=='sub'):
                if(re.search(pattern,data.get(key)) != None):
                    base64_str = data.get("md5")  
                    hex_str = base64_to_hex(base64_str)
                    list.append(hex_str)
            
with open("/Users/parthgaba/Desktop/Twitter/4plebs_data/June_file", "r") as f:
    for line in f:
        data = json.loads(line)
        
        for key in data.keys():
            if(key=='sub'):
                if(re.search(pattern,data.get(key)) != None):
                    base64_str = data.get("md5")  
                    hex_str = base64_to_hex(base64_str)
                    list.append(hex_str)
        # Process the data

with open("/Users/parthgaba/Desktop/Twitter/4plebs_data/July_file", "r") as f:
    for line in f:
        data = json.loads(line)
        
        for key in data.keys():
            if(key=='sub'):
                if(re.search(pattern,data.get(key)) != None):
                    base64_str = data.get("md5")  
                    hex_str = base64_to_hex(base64_str)
                    list.append(hex_str)
print(list)
print(len(list))

