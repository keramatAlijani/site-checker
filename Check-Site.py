import requests
import os

file = open("filter-domains.txt","w")
file.close()

with open("domains.txt") as f:
    for line in f:
        line = line.strip()
        https = "https://" + line
        try:
         passr = requests.get(https,verify=False)
         with open('filter-domains.txt', 'a') as file:
          file.write(https+"\n")
         source_https = passr.content
         http = "http://" + line
         try:
          passr = requests.get(http)
          source_http = passr.content
          if  len(source_http) == len(source_https):
           pass
          else:
            with open('filter-domains.txt', 'a') as file:
             file.write(http+"\n")
         except:
          continue

        except:
         http = "http://" + line
         try:
          passr = requests.get(http)
          with open('filter-domains.txt', 'a') as file:
           file.write(http+"\n")
         except:
          continue

