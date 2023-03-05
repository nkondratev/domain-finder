#!/bin/python3
import dns.resolver
import whois

with open('domains1.txt') as domains:
    for domain in domains:
        domain = domain.strip() + ".ru"
        try:
            result = dns.resolver.resolve(domain)
        except KeyboardInterrupt:
            break
        except:
            try:
                result = whois.whois(domain)
            except:
                print("Есть домен", domain)

        