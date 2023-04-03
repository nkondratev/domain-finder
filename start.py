#!/bin/python3

import threading
import dns.resolver
import whois
import random
import string
import time

zone = ".ru"

def part_domain(fzone):
    domain = ''
    for i in range(3):
        domain += random.choice(string.ascii_lowercase + string.digits)
    domain += fzone
    return domain

def main_domain():
        domain_name = part_domain(zone)
        try:
            result = dns.resolver.resolve(domain_name)
        except KeyboardInterrupt:
            quit()
        except:
            try:
                result = whois.whois(domain_name)
            except:
                print("Domain found", domain_name)

while True:
    for i in range(5):
        my_thread = threading.Thread(
            target=main_domain, args=())
        my_thread.start()
    for i in range(5):
        my_thread.join()
