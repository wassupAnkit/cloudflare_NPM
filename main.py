import os
# from cloudflare import Cloudflare
#ask for subdomain
default = 1
subdomain = input("Enter sudomain...")
public_ip = input("Enter public IP")
description = input("Add description here if you would like")

#ask if they just want to add it in Cloudflare
just_cloudflare = input("Do you just want to add subdomain in cloudlfare?")

if just_cloudflare == True:
    default
    #just run the program
else:
    default = 2
    #nginx_proxy_manager()
    #else call the function that also implements the given subdomain to the nginx proxy manager

#create dns record in cloudflare
def create_dns_record():
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