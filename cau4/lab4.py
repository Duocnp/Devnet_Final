import requests
import json
import meraki_info
requests.packages.urllib3.disable_warnings()
baseUrl=meraki_info.URL
API_key=meraki_info.API
org_id = "681155"
def get_org():
    url = baseUrl + f"/organizations/{org_id}/inventory/devices"
    header = {
        "X-Cisco-Meraki-API-Key" : API_key
    }
    response= requests.get(url,headers=header,verify=False)
    data=response.json()
    parse_data=json.dumps(data,indent=4)

    print(parse_data)
    # print(data)
    # print(type(data))
    device_null=[]
    for i in data:
        if i['networkId']==None:
            device_null.append(i)
            
    print(json.dumps(device_null, indent=4)) 
    
if __name__ == "__main__":
    get_org()
