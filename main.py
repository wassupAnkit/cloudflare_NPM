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


#################################################################################################################################################################


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
def create_dns_record(zone_id, email, api_token):
    ask_content = input("Enter the public ip") 
    ask_domain = input ("Enter the complete_domain, Eg: google.com")
    proxy = input("Do you want to proxy this domain? \n Y/n")
    if proxy == "Y" or "y" or "":
        proxy = True
    else:
        proxy == False
    comment_dns = input("Enter the comment if you want to add any")
    record_type = input("What kind of record do you want to enter? Example.... A, AAA, MX")
    try:
        headers = {"X-Auth-Email": email,
        "X-Auth-Key": api_token,
        "comment": comment_dns,
        "content": ask_content,
        "name": ask_domain,
        "proxied": lower(proxy),
        "ttl": 3600,
        "type": record_type
    }
        url = requests.post("https://api.cloudflare.com/client/v4/zones/zone_id/dns_records", headers=headers)
        return print("mission passed")
    except:
        return print("mission failed!",  headerss)


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
    email = os.environ.get('CLOUDFLARE_EMAIL')#input("Enter your cloudflare email")
    api_token = os.environ.get('CLOUDFLARE_API_TOKEN')
    zone_id = input("Enter your zone id, different for each domains")
    if verify_token(api_token) == 1:
        ask = input("do you want to create a new dns record now?")
        if ask == "Y" or "y" or "":
            create_dns_record(zone_id, email,api_token)
        else:
            print("don't create then get out")
    else:
        print('messed up!, but guess what Global API tokens cannot be validated.')
        create_dns_record(zone_id, email,api_token)
    

if __name__ == '__main__':
    main()
