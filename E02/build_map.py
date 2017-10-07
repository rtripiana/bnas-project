#!/usr/bin/python
import sys
import json

result = {} 
def main(argv):
   hosts = []
   for i in argv:
      hosts.append(i)
   y = 0
   for h in hosts:
      result[h] = []
      x = y
      while x < len(hosts):
         if h != hosts[x]:
            result[h].append(hosts[x])
         x += 1
      y += 1 
   result_str = json.dumps(result)
   print result_str;

if __name__ == "__main__":
   main(sys.argv[1:])
