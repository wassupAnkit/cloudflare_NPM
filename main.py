import os
import requests

# from cloudflare import Cloudflare
#ask for subdomain__
# default = 1
# subdomain = input("Enter sudomain...")
# public_ip = input("Enter public IP")
# description = input("Add description here if you would like")

# #ask if they just want to add it in Cloudflare
# just_cloudflare = input("Do you just want to add subdomain in cloudlfare?")

# if just_cloudflare == True:
#     default
#     #just run the program
# else:
    # default = 2s
    #nginx_proxy_manager()
    #else call the function that also implements the given subdomain to the nginx proxy manager


##############################################################################################################################################
#ask email and api token


def verify_token(auth_token):
    try:
        headers = {
        'Authorization': 'Bearer auth_token',
        'Content-Type': 'application/json'
        } 
        url = requests.get("https://api.cloudflare.com/client/v4/user/tokens/verify", headers=headers)
        print(url.status_code)
        if url.status_code == 200:
            return 0
        else:
            return 1
    except:
        print("Your token is invalid, recheck your token")

#create dns record in cloudflare
def create_dns_record(zone_id):
    
    headers = {"X-Auth-Email": "CLOUDFLARE_EMAIL",
    "X-Auth-Key": "CLOUDFLARE_API_KEY",
    "comment": "Domain verification record",
      "content": "198.51.100.4",
      "name": "example.com",
      "proxied": true,
      "ttl": 3600,
      "type": "A"
    }
    url = "https://api.cloudflare.com/client/v4/zones/zone_id/dns_records"
    return null


#Function to integrate with nginx proxy manager
def nginx_proxy_manager():
    
    return null 


def create_proxy():
    
    return null

def delete_proxy():
    return null

def update_proxy():
    return null 

def main():
    email = os.environ.get(CLOUDFLARE_EMAIL)#input("Enter your cloudflare email")
    api_token = os.environ.get(CLOUDFLARE_API_TOKEN)
    if verify_token(api_token) == 1:
        print(1)
    else:
        print('messed up!')

if __name__ == '__main__':
    main()
