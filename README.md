# bnas-project
Work assignments for Building Network Automation Solution training @ipspace

## Folder E01
Hands-on exercise for week1. Create a Github repository, including readme file and commit and push a file with lab description.

## Folder E02
Hands-on exercise for week2. Create a report. Consists basically of 2 files:
  * Python script: *build_map.py*
  * Ansible's Playbook: *latency_report.yml*
- **build_map.py**
Takes a list of hosts (IP or hostnames) and returns a dictionary as JSON formatted string with the optimized list of pairs. i.e., if the host list is "H1, H2, H3, H4 and H5", the returned dict is:
```
H1: [H2, H3, H4, H5]
H2: [H3, H4, H5]
H3: [H4, H5]
H4: [H5]
```
- **latency_report.yml**
  - The Playbook, takes a list of hosts and get the minimum pair sets to test RTT latency (ping).
  - Send the list to the *build_map.py* script and get the dictionary to iterate through
  - Launch the ping job on all specified hosts
  - Capture the results for each host and save them in individual files

It is assumed that there is the target Ansible's hosts file includes an alias named "ansible_host"

So far only supported for Cisco IOS devices
